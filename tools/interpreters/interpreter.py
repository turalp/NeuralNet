from keras.models import Model
from keras.layers import Input, InputLayer, Dense, LeakyReLU
from enums.NodeType import NodeType

from models.neural_net import NeuralNet
from static.static_values import input_layer_id

import tensorflow as tf

class Interpreter:
    def __init__(self) -> None:
        pass

    def interpret(self, neural_net: NeuralNet) -> Model:
        nodes = self.__process_nodes__(neural_net=neural_net)
        connections = self.__process_connections__(neural_net=neural_net)
        layers = self.__process_layers__(nodes, connections)

        input_nodes = [node.id for node in neural_net.graph_nodes if node.type == NodeType.IN]
        inputs = Input(shape=(len(input_nodes),))
        x = inputs
        for layer_num in sorted(layers.keys()):
            if layer_num == 1:
                continue

            layer_connections = layers[layer_num]
            units = len(layer_connections)
            weights = [conn['weight'] for conn in layer_connections]

            x = Dense(units, use_bias=False)(x)
            x.set_weights([tf.constant([[w] for w in weights])])

            if nodes[layer_connections[0]['target']]['type'] == 3:
                if neural_net.activation_function.name == 'LeakyReLU':
                    x = LeakyReLU()(x)

        outputs = x
        model = Model(inputs=inputs, outputs=outputs)
        return model

    def __process_inputs__(self, neural_net: NeuralNet) -> list[InputLayer]:
        input_nodes = [node_id for node_id, node in neural_net.graph_nodes.items() if node.type == NodeType.IN]
        inputs = [Input(shape=(1,), name=f"input_{node_id}") for node_id in input_nodes]
        return inputs

    def __process_layers__(self, nodes: dict, connections: list) -> dict:
        layers = {}
        for connection in connections:
            source, target, weight = connection['source'], connection['target'], connection['weight']
            source_node, target_node = nodes[source], nodes[target]
            source_layer, target_layer = source_node['layer'], target_node['layer']

            if target_layer not in layers:
                layers[target_layer] = []

            layers[target_layer].append({
                'source': source,
                'target': target,
                'weight': weight
            })

        return layers

    def __process_nodes__(self, neural_net: NeuralNet) -> dict:
        nodes = {}
        for node in neural_net.graph_nodes:
            nodes[node.id] = {
                'type': int(node.type.value),
                'layer': int(node.layer)
            }
        
        return nodes

    def __process_connections__(self, neural_net: NeuralNet) -> list:
        connections = []
        for connection in neural_net.connections:
            connections.append({
                'source': connection.source,
                'target': connection.target,
                'weight': connection.weight,
                'type': connection.type
            })
        
        return connections
    
    