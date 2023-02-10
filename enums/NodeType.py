from enum import Enum

class NodeType(Enum):
    BIAS = 0
    IN = 1
    OUT = 2,
    HID = 3

    def __str__(self) -> str:
        return str(self.value)