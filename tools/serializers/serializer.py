from abc import ABC, abstractmethod

class Serializer(ABC):

    @abstractmethod
    def serialize(self) -> str:
        pass