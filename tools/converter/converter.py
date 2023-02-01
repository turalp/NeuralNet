from helpers.neural_net_builder import NeuralNetBuilder
from helpers.neural_net_deserializer import NeuralNetDeserializer
from tools.serializers.xml_serializer import XmlSerializer


path_to_file = input("Path to file: ")
input_nodes = input("Enter input nodes: ")
output_nodes = input("Enter output nodes: ")

file_to_deserialize = open(path_to_file, 'r', encoding='utf-8')
plain_text = file_to_deserialize.read()

inputs = list(map(lambda input: int(input), input_nodes.split(',')))
outputs = list(map(lambda output: int(output), output_nodes.split(',')))

deserializer = NeuralNetDeserializer(plain_text, inputs, outputs)
deserializer.deserialize()

neural_net_builder = NeuralNetBuilder(deserializer.inputs, deserializer.outputs)
neural_net = neural_net_builder\
    .with_activation_function(deserializer.function)\
    .with_connections(deserializer.nodes)\
    .with_nodes(deserializer.nodes)\
    .return_neural_net()

serializer = XmlSerializer(neural_net)
xml = serializer.serialize()

path_to_save_file = "C:\Users\tural\OneDrive\Documents\PhD\NeuralNet\examples"
with open(path_to_save_file, "w") as f:
    f.write(xml) 