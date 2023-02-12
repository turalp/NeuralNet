from deserializers.abstract.deserializer import Deserializer
from enums.NodeType import NodeType
from models.activation_function import ActivationFunction
from models.graph_connection import GraphConnection
from models.graph_node import GraphNode
from models.neural_net import NeuralNet

from xml.dom.minidom import parseString, Document

from static.tags import CONNECTION_TAG, FUNCTION_TAG, NOTE_TAG


class XmlDeserializer(Deserializer):
    neural_net: NeuralNet

    def __init__(self) -> None:
        self.neural_net = None
        super().__init__()

    def deserialize(self, xml_text: str) -> str:
        document = parseString(xml_text)
        
        self.neural_net = NeuralNet()

        self.__set_activation_function__(document)
        self.__set_connections__(document)
        self.__set_nodes__(document)

        return self.neural_net

    def __set_activation_function__(self, document: Document) -> None:
        functionElements = document.getElementsByTagName(FUNCTION_TAG)
        if len(functionElements) == 0:
            raise SyntaxError("Activation function is not found. Please, check XML file and try again.")

        self.neural_net.activation_function = ActivationFunction(int(functionElements[0].getAttribute("id")),\
            functionElements[0].getAttribute("name"))

    def __set_nodes__(self, document: Document) -> None:
        nodeElements = document.getElementsByTagName(NOTE_TAG)
        if len(nodeElements) == 0:
            raise SyntaxError("Nodes are not found. Please, check XML file and try again.")

        for nodeElement in nodeElements:
            node = GraphNode(int(nodeElement.getAttribute("id")),\
                NodeType(int(nodeElement.getAttribute("type"))),\
                int(nodeElement.getAttribute("layer")))
            self.neural_net.graph_nodes.append(node)
        
        self.neural_net.graph_nodes.sort(key=lambda node: node.layer)

    def __set_connections__(self, document: Document) -> None:
        connectionElements = document.getElementsByTagName(CONNECTION_TAG)
        if len(connectionElements) == 0:
            raise SyntaxError("Nodes are not found. Please, check XML file and try again.")

        for connectionElement in connectionElements:
            connection = GraphConnection(int(connectionElement.getAttribute("source")),\
                int(connectionElement.getAttribute("target")),\
                float(connectionElement.getAttribute("weight")))
            self.neural_net.connections.append(connection)
        
