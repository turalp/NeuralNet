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
    
    def __str__(self) -> str:
        return 'Source: ' + str(self.source) + '\t' + 'Target: ' + str(self.target) + '\t' + 'Weight: ' + str(self.weight) + '\t' + 'Type: ' + str(self.type) + '\n'