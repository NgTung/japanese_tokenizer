import MeCab

from abc import abstractmethod
from Tokenizer import Tokenizer


class JapaneseTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()
        super(JapaneseTokenizer, self).__init__()

    @abstractmethod
    def parse(self, str):
        pass


class MeCabTokenizer(JapaneseTokenizer):
    def __init__(self, tagger=''):
        super().__init__()
        self.parser = MeCab.Tagger(tagger)

    def parse(self, str):
        return self.dynamic_func_call('parse', [str])

    def parse_to_node(self, str):
        return self.dynamic_func_call('parseToNode', [str])

    def dynamic_func_call(self, func, args):
        return getattr(self.parser, func)(*args)
