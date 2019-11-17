from otranto import Lexnum

class TestBaseTen():
    text = "0_zero 9_nine 8_eight 7_seven 6_six 5_five 4_four 3_three 2_two 1_one"
    vocab = Lexnum(text)

    def test_word_power(self):
        gen = self.vocab.word_power("3_three 2_two")
        a = [(w, p) for w, p in gen]
        assert len(a) == 2
        print(a)
        assert a[0][1] == 1
        assert a[1][1] == 10

    def test_lexnum(self):
        a = self.vocab.int(self.text)
        print(self.vocab.lexicon)
        assert len(self.vocab.lexicon) == 10 == self.vocab.radix
        t = ' '.join([i for i in self.vocab.nextlex(a)])

        assert a == 1234567890
        assert t == self.text

        product = ' '.join([i for i in self.vocab.nextlex(5 * 5)])
        assert product == "5_five 2_two"

    def test_int(self):
        assert 80 == self.vocab.int('0_zero 8_eight')
        assert 81 == self.vocab.int('1_one 8_eight')
        assert 85 == self.vocab.int('5_five 8_eight')
        assert 108 == self.vocab.int('8_eight 0_zero 1_one')
