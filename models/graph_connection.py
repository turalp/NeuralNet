from enums.NodeType import NodeType

class GraphConnection:
    source: int
    target: int
    weight: float
    type: NodeType

    def __init__(self, source: int, target: int, weight: float, type: NodeType) -> None:
        self.source = source
        self.target = target
        self.weight = weight
        self.type = type