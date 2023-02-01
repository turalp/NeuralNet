from enums.NodeType import NodeType
from helpers.header_helper import HeaderHelper

from models.activation_function import ActivationFunction
from models.graph_connection import GraphConnection

from static.constants import ACTIVATION_HEADER, CONNECTION_HEADER, NODE_COUNT_HEADER

class NeuralNetDeserializer:
    text: str
    inputs: list[int]
    outputs: list[int]
    function: ActivationFunction
    nodes: list[GraphConnection]

    def __init__(self, neural_net: str, inputs: list[int], outputs: list[int]) -> None:
        self.text = neural_net
        self.inputs = inputs
        self.outputs = outputs
    
    def deserialize(self) -> None:
        lines = self.text.splitlines()
        headers = HeaderHelper()
        nodes = list()
        for line in lines:
            if str.isspace(line) or line == '':
                headers.is_activation = False
                headers.is_connections = False
                headers.is_node_type = False
                continue

            self.__process_line(line, headers, nodes)
            self.__checkHeader(line, headers)
        
        self.nodes = nodes
    
    def __process_line(self, line: str, headers: HeaderHelper, nodes: list[GraphConnection]) -> None:
        if headers.is_connections:
            params = line.split('\t')
            
            source = int(params[0])
            destination = int(params[1])
            weight = float(params[2])

            if source in self.inputs:
                node_type = NodeType.IN
            elif source in self.outputs:
                node_type = NodeType.OUT
            else:
                node_type = NodeType.HID
            nodes.append(GraphConnection(source, destination, weight, node_type))
            
        if headers.is_activation:
            params = line.split('\t')
            self.function = ActivationFunction(int(params[0]), params[1])

    def __checkHeader(self, line: str, headers: HeaderHelper) -> None:
        if line == ACTIVATION_HEADER:
            headers.is_activation = True
        
        if line == CONNECTION_HEADER:
            headers.is_connections = True
        
        if line == NODE_COUNT_HEADER:
            headers.is_node_type = True
