from otranto import Lexnum

class TestFables:
    kafka = '''"Alas," said the mouse, "the world gets smaller every day. At first it was so wide that I ran along and was happy to see walls appearing to my right and left, but these high walls converged so quickly that I’m already in the last room, and there in the corner is the trap into which I must run."

"But you’ve only got to run the other way," said the cat, and ate it.
'''

    aesop = '''A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her.

"Spare me!" begged the poor Mouse. "Please let me go and some day I will surely repay you."

The Lion was much amused to think that a Mouse could ever help him. But he was generous and finally let the Mouse go.

Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net. Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free.

"You laughed when I said I would repay you," said the Mouse. "Now you see that even a Mouse can help a Lion."
'''

    def test_kafka_vocab(self):
        vocab = Lexnum(self.kafka)
        assert len(vocab.lexicon) == 56
        print("VOCAB: %s" % {k: v for k, v in enumerate(vocab.lexicon)})

        # 10 in base-56 vocab from Kafka's Little Fable:
        assert vocab.lex(56) == '"Alas," "the'
        assert 56 == vocab.int('"Alas," "the')
        assert 1092 == vocab.int('mouse, happy')

    def test_kafka_vocab_longer(self):
        vocab = Lexnum(self.kafka)

        t = '"Alas," said the mouse, "the world gets smaller every day.'

        i = vocab.int(t)
        assert t == vocab.lex(i)  # text > int > text conversion does not lose info

        assert i & 1 == 0  # int _is_ even

        half = vocab.lex(i//2)  # Half text

        assert half == vocab.lex(vocab.int(half))  # text > int > text conversion does not lose info
        assert (i//2) == vocab.int(half)
        assert t == vocab.lex(vocab.int(half) * 2)  # Double the halved-text == original text

    def test_half_a_fable(self):
        vocab = Lexnum(self.kafka)
        k = vocab.int(self.kafka)

        # k is an even number:
        assert k & 1 == 0

        halved = vocab.lex(k // 2)
        print('### Half A Little Fable:\n')
        print(halved, '\n')

        d = 2 * vocab.int(halved)
        redoubled = vocab.lex(d)
        assert d & 1 == 0
        assert d == k

        print("### Half A Little Fable, redoubled:\n")
        print(redoubled, '\n')
        assert redoubled == self.kafka

    def test_fable_to_powers(self):
        vocab = Lexnum(self.kafka)
        k = vocab.int(self.kafka)
        out5 = vocab.lex(k ** 5)
        print('### A Little Fable to the power of 5:\n')
        print(out5, '\n')
        out6 = vocab.lex(k ** 6)
        print('### A Little Fable to the power of 6:\n')
        print(out6, '\n')
        assert out5.startswith('"Alas," "Alas," "Alas," "Alas," "Alas," is run."')  # 5 x 0-symbol
        assert out6.startswith('"Alas," "Alas," "Alas," "Alas," "Alas," "Alas,"')   # 6 x 0-symbol

    def test_vocab_expansion(self):
        vocab = Lexnum(self.kafka)
        k = vocab.int(self.kafka)
        qbf = 'The quick brown fox jumps over the lazy dog.'
        vocab2 = Lexnum(self.kafka + ' ' + qbf)
        out = vocab2.lex(k)
        print('### A Little Fable base converted into a vocabulary expansion with "%s"\n' % qbf)
        print(out, '\n')
        assert k == vocab2.int(out)

    def test_kafka_aesop_product(self):
        vocab = Lexnum(self.kafka + ' ' + self.aesop)
        k = vocab.int(self.kafka)
        a = vocab.int(self.aesop)
        out = vocab.lex(a * k)
        print("### Product of Kafka's Little Fable and an Aesop's Fable:\n")
        print(out, '\n')
        assert out.startswith('"Alas," I away, along that "Please poor wide it amused laid walls net. mouse, paws. prey soon Roused Roused there think go.')
