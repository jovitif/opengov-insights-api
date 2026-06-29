from typing import Any
import requests

from config.settings import MOSSORO_API
from connectors.base import BaseConnector

class TransparencyMossoroConnector(BaseConnector):
    @property
    def source_name(self) -> str:
        return "mossoro"

    def extract(self, endpoint: str, params: dict | None = None) -> Any:

        response = requests.get(
            f"{MOSSORO_API}/{endpoint}",
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()