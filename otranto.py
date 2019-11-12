#!/usr/bin/env python3
import sys

HALF   = {
        'source': 'texts/Otranto.txt',
        'op': lambda x: x // 2
        }
DOUBLE = {
        'source': 'texts/half.txt',
        'op': lambda x: x * 2
        }

class Lexnum():
    def __init__(self, s):
        words = set(s.split(' '))
        self.lexicon = list(sorted(words))
        self.radix = len(self.lexicon)

    def int(self, s):
        """ Returns an int based on an input string and a list of words
            representing a number system.
        """
        return sum([self.lexicon.index(w) * (self.radix ** i) for i,w in enumerate(s.split(' '))])

    def lex(self, i):
        """ inverse of above """
        output = []
        remainder = i
        while remainder > 0:
            w = remainder % self.radix
            remainder = remainder // self.radix
            output.append(self.lexicon[w])
        return ' '.join(output)


if __name__ == '__main__':

    target = DOUBLE if sys.argv[1] == 'double' else HALF
    with open(target['source'], 'r') as f:
        text = f.read()
        vocab = Lexnum(text)
        full = vocab.int(text)
        result = vocab.lex(target['op'](full))
        print(result)
