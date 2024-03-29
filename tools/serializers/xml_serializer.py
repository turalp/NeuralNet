from xml.dom.minidom import Document, Element
from models.neural_net import NeuralNet
from tools.serializers.serializer import Serializer


class XmlSerializer(Serializer):
    neural_net: NeuralNet

    def __init__(self, neural_net: NeuralNet) -> None:
        self.neural_net = neural_net

    def serialize(self) -> str:
        root = Document()
        
        xml = root.createElement("root")
        root.appendChild(xml)

        functions = self.__create_functions_section__(root)
        xml.appendChild(functions)

        nodes = self.__create_nodes_section__(root)
        xml.appendChild(nodes)

        connections = self.__create_connection_section__(root)
        xml.appendChild(connections)

        return root.toprettyxml(indent ="\t")
        

    def __create_functions_section__(self, root: Document) -> Element:
        functions = root.createElement("activationFunctions")

        function = root.createElement("function")
        function.setAttribute("id", str(self.neural_net.activation_function.id))
        function.setAttribute("name", str(self.neural_net.activation_function.name))

        functions.appendChild(function)
        return functions

    def __create_connection_section__(self, root: Document) -> Element:
        connections = root.createElement("connections")

        for connection in self.neural_net.connections:
            connectionElement = root.createElement("connection")
            
            connectionElement.setAttribute("source", str(connection.source))
            connectionElement.setAttribute("target", str(connection.target))
            connectionElement.setAttribute("weight", str(connection.weight))
            
            connections.appendChild(connectionElement)
        
        return connections

    def __create_nodes_section__(self, root: Document) -> Element:
        nodes = root.createElement("nodes")

        for node in self.neural_net.graph_nodes:
            nodeElement = root.createElement("node")

            nodeElement.setAttribute("type", str(node.type))
            nodeElement.setAttribute("id", str(node.id))
            nodeElement.setAttribute("layer", str(node.layer))

            nodes.appendChild(nodeElement)
        
        return nodes

        
