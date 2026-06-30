from pipelines.load.load_postgres import load_postgres


def run():

    load_postgres(
        parquet_path=
        "data/processed/mossoro/receita/2024.parquet",

        table_name=
        "fato_receita"
    )


if __name__ == "__main__":
    run()