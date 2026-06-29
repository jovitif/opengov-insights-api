from connectors.transparency_mossoro import TransparencyMossoroConnector
from writers.json_writer import write_json


def run(
    endpoint: str,
    params: dict,
    output_path: str,
):
    connector = TransparencyMossoroConnector()

    data = connector.extract(
        endpoint=endpoint,
        params=params,
    )

    write_json(
        data=data,
        path=output_path,
    )

    return data


if __name__ == "__main__":
    run(
        endpoint="receita",
        params={
            "periodo_inicial": "01/2024",
            "periodo_final": "12/2024",
            "codigo_unidade": 20,
        },
        output_path="data/raw/mossoro/receita/2024/receita_2024.json",
    )