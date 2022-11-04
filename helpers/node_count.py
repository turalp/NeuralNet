class NodeCount:
    input_count: int
    output_count: int
    output_node: int

    def __init__(self, output_node) -> None:
        self.output_node = output_node