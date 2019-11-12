from otranto import Lexnum

def test_lexnum():
    text = "0_zero 9_nine 8_eight 7_seven 6_six 5_five 4_four 3_three 2_two 1_one"
    vocab = Lexnum(text)
    a = vocab.int(text)
    print(vocab.lexicon)

    t = ' '.join([i for i in vocab.nextlex(a)])

    assert a == 1234567890
    assert t == text

    product = ' '.join([i for i in vocab.nextlex(5 * 5)])
    assert product == "5_five 2_two"

