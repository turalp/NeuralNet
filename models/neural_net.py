from __future__ import annotations
from helpers.node_count import NodeCount
from models.graph_connection import GraphConnection
from models.activation_function import ActivationFunction


class NeuralNet:
    connections: list[GraphConnection]
    activation_function: ActivationFunction
    node_count: NodeCount

    def __init__(self, activation_function: ActivationFunction, connections: list[GraphConnection]) -> None:
        self.activation_function = activation_function
        self.connections = connections
