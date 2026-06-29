from typing import Any
import requests

from connectors.base import BaseConnector

class TransparencyMossoroConnector(BaseConnector):

    BASE_URL = "https://transparencia.e-publica.net/epublica-portal/rest/mossoro/api/v1"

    @property
    def source_name(self) -> str:
        return "mossoro"

    def extract(self, endpoint: str, params: dict | None = None) -> Any:

        response = requests.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()