from typing import Dict
from enums.NodeType import NodeType

node_types: Dict[NodeType, str] = {
    NodeType.BIAS: "bias",
    NodeType.IN: "in",
    NodeType.OUT: "out",
    NodeType.HID: "hid"
}