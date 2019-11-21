#!/usr/bin/env python3

# script to convert the raw halved and redoubled Otranto texts
# into publishable markdown, for conversion into pdf
# output to STDOUT

import re

headings = ["""# Book the First: The Castle of Otranto, Halved.

> Being _The Castle of Otranto_  by Horace Walpole, interpreted as a large integer and divided by two in the number system implied by its sorted symbols as separated by spaces in the text.
""",
"""# Book the Second: The Castle of Otranto, Reconstructed.

> Being the first book in this sequence, _The Castle of Otranto, Halved_, interpreted as a large integer and _multiplied_ by two in the number system implied by **_its own_** sorted symbols as separated by spaces in the text in a vain attempt to reconstruct the original text, _The Castle of Otranto_, by Horace Walpole.

"""
]


R = 'IV XL CD M.'
A = [1,4];[A.append(sum(A[-2:])) for i in A*1]

def to_roman(t):
    """
    ridiculous!
    """
    o = ''
    for c in zip([i*10**n for n in range(4) for i in A][::-1], o.join([f'{p[0]} '*2+f'{p} {p[1]} {p[0]}' for p in R.split()]).split()[::-1]):
        k = t // c[0]
        o += c[1] * k
        t -= c[0] * k
    return o


def firstcap(s):
    """
    Capitalise the first letter of a string/sentence.
    """
    return s[0].upper() + s[1:]


def make_chapter(s):
    """
    Makes a sentence into a chapter heading.
    """
    title = s.replace('CHAPTER ', '')
    # if title has more than one sentence, split:
    m = re.match(r'(^[^\.\?!]*[\.\?!]?)(.*)$', title)
    if m:
        title = m.group(1).title().replace("’S", "’s")
        if m.group(2):
            title += '\n\n' + firstcap(m.group(2).strip())
    return '## CHAPTER %s: %s' % (to_roman(next_chapter), title)


if __name__ == '__main__':
    fnames = ['texts/half.txt', 'texts/double.txt']

    for i, fname in enumerate(fnames):
        begin = True
        next_chapter = 1
        print(headings[i])
        with open(fname, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if (line and begin) or 'CHAPTER' in line:
                    line = make_chapter(('CHAPTER ' if begin else '') + line)
                    next_chapter += 1
                    begin = False
                print(line)
        print('\n***\n')

