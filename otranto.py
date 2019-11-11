#!/usr/bin/env python3

source_file="Otranto.txt"
#source_file="half.txt"


def numbersystem(s1, s2=''):
    words = set(s1.split(' '))
    words.update(set(s2.split(' ')))
    return list(sorted(words))


def words2int(s, words):
    """ Returns an int based on an input string and a list of words
        representing a number system.
    """
    radix = len(words)
    return sum([words.index(w) * (radix ** i) for i,w in enumerate(s.split(' '))])


def int2words(i, words):
    """ inverse of above """
    radix = len(words)
    output = []
    remainder = i
    while remainder > 0:
        w = remainder % radix
        remainder = remainder // radix
        #output.append("%d:%s" % (w, words[w]))
        output.append(words[w])
    return ' '.join(output)


with open(source_file, 'r') as f:
    text = f.read()
    vocab = numbersystem(text)
    #print(len(vocab))
    full = words2int(text, vocab)

    half = int2words(full//2, vocab)
    #double = int2words(full*2, vocab)
    
    print(half)
    #print(double)
