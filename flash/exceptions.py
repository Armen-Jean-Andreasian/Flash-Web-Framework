class PathOccupied(Exception):
    def __init__(self, path: str):
        self.path = path

    def __str__(self):
        return f"{self.path} is already occupied."
