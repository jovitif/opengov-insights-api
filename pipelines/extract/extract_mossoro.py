from connectors.transparency_mossoro import TransparencyMossoroConnector
from writers.json_writer import write_json

def extract(
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