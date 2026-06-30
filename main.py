from pprint import pprint

from pydantic import json

from connectors.transparency_mossoro import TransparencyMossoroConnector
from pipelines import extract
from pipelines.load import load_postgres
from pipelines.transform import transform_receita
from writers.parquet_writer import write_parquet


def main():

    extract(
        endpoint="receita",
        params={
            "periodo_inicial": "01/2024",
            "periodo_final": "12/2024",
            "codigo_unidade": 20,
        },
        output_path="data/raw/mossoro/receita/2024/receita_2024.json",
    )


    with open(
        "data/raw/mossoro/receita/2024/receita_2024.json",
        encoding="utf-8"
    ) as f:
        raw = json.load(f)

    dados_transformados = transform_receita(raw)

    write_parquet(dados_transformados)

    load_postgres(
        "data/processed/receita.parquet",
        "receitas"
    )

if __name__ == "__main__":
    main()