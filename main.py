from pprint import pprint

from connectors.transparency_mossoro import TransparencyMossoroConnector


def main():
    connector = TransparencyMossoroConnector()

    data = connector.extract(
        "receita",
        params={
            "periodo_inicial": "01/2024",
            "periodo_final": "12/2024",
            "codigo_unidade": 20,
        },
    )

    print(type(data))
    pprint(data)


if __name__ == "__main__":
    main()