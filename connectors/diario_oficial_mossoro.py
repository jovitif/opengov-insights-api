from typing import Any

import requests

from config.settings import DIARIO_OFICIAL_MOSSORO
from connectors.base import BaseConnector

class DiarioOficialMossoroConnector(BaseConnector):
    @property
    def source_name(self) -> str:
        return "diario_oficial_mossoro"

    def extract(self, **kwargs) -> Any:
        timeout = kwargs.get("timeout", 30)

        response = requests.get(
            DIARIO_OFICIAL_MOSSORO,
            timeout=timeout,
        )

        response.raise_for_status()

        return response.text