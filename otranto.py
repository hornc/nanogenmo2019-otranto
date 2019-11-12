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
        """
        Returns an int based on an input string and a list of words
        representing a number system.
        """
        return sum([self.lexicon.index(w) * p for w,p in self.word_power(s)])

    def lex(self, i):
        """
        Returns a full lex string representing integer i.
        """
        return ' '.join([d for d in self.nextlex(i)])

    def nextlex(self, i):
        """
        Generator which yields the next lex digit of integer i.
        """
        remainder = i
        while remainder > 0:
            w = remainder % self.radix
            remainder = remainder // self.radix
            yield self.lexicon[w]

    def word_power(self, s):
        words = s.split(' ')
        i = 0
        p = 1
        while i < (len(words) - 1):
            p *= self.radix
            i += 1
            yield words[i], p


if __name__ == '__main__':

    target = DOUBLE if sys.argv[1] == 'double' else HALF
    with open(target['source'], 'r') as f:
        text = f.read()
        vocab = Lexnum(text)
        full = vocab.int(text)
        result = vocab.nextlex(target['op'](full))
        for word in result:
            print(word + ' ', end='')
