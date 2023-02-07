from enums.NodeType import NodeType

class GraphNode:
    id: int
    type: NodeType
    graph_inputs: list
    layer: int

    def __init__(self, id: int, type: NodeType, inputs: list[int], layer: int) -> None:
        self.id = id
        self.type = type
        self.graph_inputs = inputs
        self.layer = layer
    
    def __str__(self) -> str:
        return 'Id: ' + str(self.id) + '\t' + 'Type: ' + str(self.type) + '\t' + 'Inputs: '.join([str(input) for input in self.graph_inputs])