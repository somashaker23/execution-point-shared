import uuid
from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def convert(self, chat_data: dict) -> dict:
        """Convert input chat format to the internal standard format."""
        pass

    @abstractmethod
    def get_client_name(self) -> str:
        """Convert input chat format to the internal standard format."""
        pass

    def get_vocab_id(self) -> str:
        """TODO: check if uuid can produce duplicate values. if yes, then use a different method."""
        return 'VOC' + str(uuid.uuid4())

