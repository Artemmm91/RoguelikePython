from abc import ABCMeta, abstractmethod
from graphics.interface import InterfacePyGame


class Process(metaclass=ABCMeta):
    interface = InterfacePyGame()

    @abstractmethod
    def main_loop(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def process_events(self):
        pass
