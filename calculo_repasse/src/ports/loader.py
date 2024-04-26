from typing import Protocol


class Loader(Protocol):
    def load(self) -> None:
        pass


class FileLoader:
    def __init__(self) -> None:
        self.loader = None

    def inject_loader(self, loader: Loader) -> None:
        assert loader, 'Invalid loader provided'
        self.loader = loader

    def extract(self) -> None:
        self.loader.load()
