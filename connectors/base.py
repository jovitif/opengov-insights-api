from abc import ABC, abstractmethod
from typing import Any


class BaseConnector(ABC):
    @property
    @abstractmethod
    def source_name(self) -> str:
        pass

    @abstractmethod
    def extract(self, **kwargs) -> Any:
        pass