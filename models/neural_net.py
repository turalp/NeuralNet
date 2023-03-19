from __future__ import annotations
from collections import defaultdict
from enums.NodeType import NodeType
from helpers.node_count import NodeCount
from models.graph_connection import GraphConnection
from models.activation_function import ActivationFunction
from models.graph_node import GraphNode


class NeuralNet:
    connections: list[GraphConnection]
    graph_nodes: dict[int, dict[NodeType, int]]
    activation_function: ActivationFunction
    nodes: NodeCount
    layers: defaultdict(list[int])

    def __init__(self, activation_function: ActivationFunction=None, connections: list[GraphConnection]=None) -> None:
        self.activation_function = activation_function
        self.connections = list[GraphConnection]() if connections is None else connections
        self.graph_nodes = dict[int, dict[NodeType, int]]()
        self.nodes = NodeCount()
        self.layers = defaultdict(list[int])
    
    def __str__(self) -> str:
        return ''.join([str(connection) for connection in self.connections]) + '\n'\
            + ''.join([str(node) for node in self.graph_nodes]) + '\n'\
            + str(self.activation_function)
