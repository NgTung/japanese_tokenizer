from abc import ABC, abstractmethod


class Tokenizer(ABC):
    def __init__(self):
        super(Tokenizer, self).__init__()

    @abstractmethod
    def parse(self, str):
        pass

