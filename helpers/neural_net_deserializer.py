from enums.NodeType import NodeType
from helpers.header_helper import HeaderHelper

from models.activation_function import ActivationFunction
from models.graph_connection import GraphConnection
from models.neural_net import NeuralNet

from static.constants import ACTIVATION_HEADER, CONNECTION_HEADER, NODE_COUNT_HEADER

class NeuralNetDeserializer:
    def __init__(self, neural_net: str) -> None:
        self.text = neural_net
    
    def deserialize(self) -> NeuralNet:
        lines = self.text.splitlines()
        headers = HeaderHelper()
        neural_net = NeuralNet()
        for line in lines:
            self.__process_line(line, headers, neural_net)
            self.__checkHeader(line, headers)

        return neural_net
    
    def __process_line(self, line: str, headers: HeaderHelper, neural_net: NeuralNet) -> None:
        if headers.is_connections:
            params = line.split('\t')
            if sum(connection.source == params[0] for connection in neural_net.connections) < neural_net.node_count.input_count:
                node_type = NodeType.IN
            elif params[0] == neural_net.node_count.output_node:
                node_type = NodeType.OUT
            else:
                node_type = NodeType.HID
            neural_net.connections.append(GraphConnection(params[0], params[1], params[2], node_type))
            
        if headers.is_activation:
            params = line.split('\t')
            neural_net.function = ActivationFunction(params[0], params[1])
            
        if headers.is_node_type:
            params = line.split('\t')
            neural_net.node_count.input_count = params[0]
            neural_net.node_count.output_count = params[1]

    def __checkHeader(self, line: str, headers: HeaderHelper) -> None:
        if line == ACTIVATION_HEADER:
            headers.is_activation = True
        
        if line == CONNECTION_HEADER:
            headers.is_connections = True
        
        if line == NODE_COUNT_HEADER:
            headers.is_node_type = True

        if str.isspace(line):
            headers.is_activation = False
            headers.is_connections = False
            headers.is_node_type = False