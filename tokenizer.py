import MeCab


class Token:
    def __init__(self, node):
        self.surface = node.surface
        self.part_of_speech = node.feature


class Tokenizer:
    def __init__(self):
        mecab_args = ' '.join(['-d', '/usr/lib/mecab/dic/mecab-ipadic-neologd'])
        self._t = MeCab.Tagger(mecab_args)
        self._t.parse('')

    def tokenize(self, text: str):
        node = self._t.parseToNode(text)

        tokens = []
        while node:
            if node.surface:
                tokens.append(Token(node))
            node = node.next
            
        return tokens
