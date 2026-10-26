"""Auditoria reproduzível dos Exhibits do case Vitaliza.

Uso:
    uv run --with duckdb --with pytz python src/01_auditoria_data_room.py
    uv run --with duckdb --with pytz python src/01_auditoria_data_room.py --json relatorios/auditoria.json

O script publica apenas agregados. Nenhum e-mail, texto livre ou identificador individual
é exibido na saída.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import duckdb

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_DIR = ROOT / "documentos" / "exhibits-m2"
CUTOFF = "2026-09-30"

EXPECTED_ROWS = {
    "usuarios.csv": 64_948,
    "assinaturas.csv": 32_643,
    "amizades.csv": 113_480,
    "campanha_ago26.csv": 14_120,
    "eventos_assinatura.csv": 275_565,
    "pagamentos.csv": 165_548,
    "uso_mensal.csv": 591_662,
    "atividades.parquet": 1_254_475,
    "onboarding.csv": 63_929,
    "pesquisa_saida.csv": 643,
    "feed_posts.csv": 119_309,
    "tickets_suporte.csv": 4_422,
}

PRIMARY_KEYS = {
    "usuarios.csv": "user_id",
    "assinaturas.csv": "assinatura_id",
    "campanha_ago26.csv": "user_id",
    "pagamentos.csv": "pagamento_id",
    "onboarding.csv": "onboarding_id",
    "pesquisa_saida.csv": "resposta_id",
    "feed_posts.csv": "post_id",
    "tickets_suporte.csv": "ticket_id",
    "atividades.parquet": "atividade_id",
}


def sql_path(path: Path) -> str:
    return str(path).replace("'", "''")


def relation(data_dir: Path, filename: str) -> str:
    path = sql_path(data_dir / filename)
    if filename.endswith(".parquet"):
        return f"read_parquet('{path}')"
    return f"read_csv_auto('{path}', header=true, sample_size=-1)"


def rows(connection: duckdb.DuckDBPyConnection, query: str) -> list[dict[str, Any]]:
    cursor = connection.execute(query)
    names = [column[0] for column in cursor.description]
    return [dict(zip(names, item, strict=True)) for item in cursor.fetchall()]


def scalar(connection: duckdb.DuckDBPyConnection, query: str) -> Any:
    return connection.execute(query).fetchone()[0]


def audit(data_dir: Path) -> dict[str, Any]:
    missing = [name for name in EXPECTED_ROWS if not (data_dir / name).exists()]
    if missing:
        return {"status": "failed", "data_dir": str(data_dir), "missing": missing}

    connection = duckdb.connect()
    inventory: list[dict[str, Any]] = []
    count_mismatches: list[dict[str, Any]] = []

    for filename, expected in EXPECTED_ROWS.items():
        found = scalar(connection, f"SELECT count(*) FROM {relation(data_dir, filename)}")
        inventory.append({"file": filename, "expected": expected, "found": found})
        if found != expected:
            count_mismatches.append(
                {"file": filename, "expected": expected, "found": found}
            )

    duplicate_keys: dict[str, int] = {}
    for filename, key in PRIMARY_KEYS.items():
        rel = relation(data_dir, filename)
        duplicate_keys[filename] = scalar(
            connection,
            f"SELECT count(*) - count(DISTINCT {key}) FROM {rel}",
        )

    subscriptions = relation(data_dir, "assinaturas.csv")
    active = rows(
        connection,
        f"""
        SELECT
          count(*) FILTER (WHERE status_atual = 'ativa') AS active_total,
          count(*) FILTER (
            WHERE status_atual = 'ativa' AND plano_atual IN ('mensal', 'anual')
          ) AS active_paid,
          count(*) FILTER (
            WHERE status_atual = 'ativa' AND plano_atual = 'cortesia'
          ) AS active_courtesy
        FROM {subscriptions}
        """,
    )[0]

    users = relation(data_dir, "usuarios.csv")
    feed = relation(data_dir, "feed_posts.csv")
    friends = relation(data_dir, "amizades.csv")
    activities = relation(data_dir, "atividades.parquet")

    post_cutoff = {
        "usuarios.csv": scalar(
            connection,
            f"SELECT count(*) FROM {users} WHERE data_cadastro >= DATE '2026-10-01'",
        ),
        "feed_posts.csv": scalar(
            connection,
            f"SELECT count(*) FROM {feed} WHERE data_hora >= TIMESTAMP '2026-10-01'",
        ),
        "amizades.csv": scalar(
            connection,
            f"SELECT count(*) FROM {friends} WHERE desde >= DATE '2026-10-01'",
        ),
        "atividades.parquet": scalar(
            connection,
            f"""
            SELECT count(*) FROM {activities}
            WHERE try_cast(inicio AS TIMESTAMP) >= TIMESTAMP '2026-10-01'
            """,
        ),
    }

    system_categories = rows(
        connection,
        f"SELECT sistema, count(*) AS rows FROM {users} GROUP BY 1 ORDER BY rows DESC",
    )
    activity_categories = rows(
        connection,
        f"SELECT tipo, count(*) AS rows FROM {activities} GROUP BY 1 ORDER BY rows DESC",
    )

    result = {
        "status": "passed_with_warnings",
        "data_dir": str(data_dir),
        "cutoff": CUTOFF,
        "inventory": inventory,
        "count_mismatches": count_mismatches,
        "duplicate_primary_keys": duplicate_keys,
        "active_subscriptions": active,
        "post_cutoff_rows": post_cutoff,
        "category_quality": {
            "sistema": system_categories,
            "atividade_tipo": activity_categories,
        },
    }

    if count_mismatches or any(duplicate_keys.values()):
        result["status"] = "failed"

    return result


def print_human(report: dict[str, Any]) -> None:
    print("=" * 78)
    print("AUDITORIA DOS EXHIBITS — CASE VITALIZA")
    print(f"Diretório: {report['data_dir']}")
    print(f"Status: {report['status']}")
    print("=" * 78)

    if report["status"] == "failed" and "missing" in report:
        for filename in report["missing"]:
            print(f"[FALHA] arquivo ausente: {filename}")
        return

    for item in report["inventory"]:
        marker = "OK" if item["expected"] == item["found"] else "FALHA"
        print(
            f"[{marker}] {item['file']:<24} "
            f"esperado={item['expected']:>9,} encontrado={item['found']:>9,}"
        )

    active = report["active_subscriptions"]
    print("\nReconciliação da base ativa")
    print(f"- ativas totais: {active['active_total']:,}")
    print(f"- pagantes mensais/anuais: {active['active_paid']:,}")
    print(f"- cortesias: {active['active_courtesy']:,}")

    print("\nRegistros posteriores ao corte de 30/09/2026")
    for filename, count in report["post_cutoff_rows"].items():
        print(f"- {filename}: {count:,}")

    duplicates = sum(report["duplicate_primary_keys"].values())
    print(f"\nDuplicidades nas chaves testadas: {duplicates:,}")
    print("Avisos de categoria: sistema operacional e tipo de atividade exigem normalização.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--json", type=Path, help="Salva também o relatório em JSON")
    args = parser.parse_args()

    report = audit(args.data_dir)
    print_human(report)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n",
            encoding="utf-8",
        )
        print(f"\nJSON salvo em: {args.json}")

    return 1 if report["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
