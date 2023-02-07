class HeaderHelper:
    is_activation: bool
    is_connections: bool
    is_node_type: bool
    is_layers: bool

    def __init__(self) -> None:
        self.is_activation = False
        self.is_connections = False
        self.is_node_type = False
        self.is_layers = False        