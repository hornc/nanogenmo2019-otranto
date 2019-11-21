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
        return sum([v * p for v,p in self.word_power(s)])

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
        """
        Given a input string of word symbols, returns a generator (symbol-value, multiplier).
        """
        words = s.split(' ')
        i = 0
        p = 1
        least_sig = True
        while i < len(words):
            if not least_sig:
                p *= self.radix
            else:
                least_sig = False
            i += 1
            yield self.lexicon.index(words[i-1]), p


if __name__ == '__main__':

    target = DOUBLE if len(sys.argv) > 1 and sys.argv[1] == 'double' else HALF
    with open(target['source'], 'r') as f:
        text = f.read()
        vocab = Lexnum(text)
        full = vocab.int(text)
        result = vocab.nextlex(target['op'](full))
        separator = ''
        for word in result:
            print(separator + word, end='')
            if separator == '':
                separator = ' '
        print('')
