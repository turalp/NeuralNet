class ActivationFunction:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
    
    def __str__(self) -> str:
        return self.name