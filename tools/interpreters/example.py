import xml.etree.ElementTree as ET
import tensorflow as tf
from keras.layers import Input, Dense, LeakyReLU
from keras.models import Model
from collections import defaultdict

# Parse the XML
xml_str = '''
# [Paste the entire XML content here]
'''
root = ET.fromstring(xml_str)

# Extract activation functions
activation_functions = {}
for function in root.find("activationFunctions"):
    activation_functions[int(function.get("id"))] = function.get("name")

# Extract nodes and layers
nodes = {}
layers = defaultdict(list)
for node in root.find("nodes"):
    node_id = int(node.get("id"))
    node_type = int(node.get("type"))
    layer = int(node.get("layer"))
    nodes[node_id] = {"type": node_type, "layer": layer}
    layers[layer].append(node_id)

# Extract connections
connections = []
for connection in root.find("connections"):
    source = int(connection.get("source"))
    target = int(connection.get("target"))
    weight = float(connection.get("weight"))
    connections.append((source, target, weight))

# Create TensorFlow model using the Functional API
input_nodes = [node_id for node_id, node in nodes.items() if node["layer"] == 1]
output_nodes = [node_id for node_id, node in nodes.items() if node["layer"] == max(layers)]

inputs = [Input(shape=(1,), name=f"input_{node_id}") for node_id in input_nodes]
layer_outputs = {node_id: inputs[input_nodes.index(node_id)] for node_id in input_nodes}

for layer in range(2, max(layers) + 1):
    for node_id in layers[layer]:
        node_type = nodes[node_id]["type"]

        if node_type == 1:  # Linear
            continue
        elif node_type == 2:  # Output
            layer_input = layer_outputs[connections[0][0]]
            for source, target, weight in connections:
                if target == node_id:
                    layer_input += layer_outputs[source] * weight
            layer_outputs[node_id] = layer_input
        elif node_type == 3:  # Activation
            activation_function = activation_functions[0]
            layer_input = layer_outputs[connections[0][0]]
            for source, target, weight in connections:
                if target == node_id:
                    layer_input += layer_outputs[source] * weight
            if activation_function == "LeakyReLU":
                layer_outputs[node_id] = LeakyReLU()(layer_input)

output = [layer_outputs[node_id] for node_id in output_nodes]
model = Model(inputs=inputs, outputs=output)

# Display the model summary
model.summary()


