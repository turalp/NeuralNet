from keras.models import Model
from keras.layers import Input, InputLayer, Dense

from models.neural_net import NeuralNet
from static.static_values import input_layer_id

class Interpreter:


    def __init__(self) -> None:
        pass

    def interpret(self, neural_net: NeuralNet) -> Model:
        inputs = self.__process_inputs__(neural_net=neural_net)


        pass

    def __process_inputs__(self, neural_net: NeuralNet) -> list[InputLayer]:
        input_nodes = [node_id for node_id, node in neural_net.graph_nodes.items() if node["layer"] == 1]
        inputs = [Input(shape=(1,), name=f"input_{node_id}") for node_id in input_nodes]
        return inputs

    def __process_nodes__(self) -> None:
        pass

    def __process_connections__(self) -> None:
        pass

    def __process_outputs(self) -> None:
        pass