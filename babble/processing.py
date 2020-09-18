from os import urandom
import os.path

import babble.wordlist

WORDLIST = babble.wordlist.WORDLIST

def check_list(_list):
    """ usage: check_list(_list)

        Raises ValueError if _list is somehow unsuitable for use.
        Tests for length, duplicates, and whitespace related issues"""
    length = len(_list)
    if length != 4096:
        message = "list must be exactly 4096 entries (got {})"
        raise(ValueError(message.format(length)))
    if len(set(_list)) != length:
        raise(ValueError("list contains duplicate entries"))

    length2 = len([word for word in _list if word.strip() and
                   len(word.split(' ')) == 1])
    if length != length2:
        raise(ValueError("Word list contains unsuitable entries (i.e. spaces)"))

def sample(_list, n):
    """ usage: sample(_list, n): => n random elements of _list

        Outputs n elements of _list, chosen uniformly at random.
        Parameters are hard-coded. Only supports lists with 4096 entries. """
    check_list(_list)
    output = []; length = 4096          # bits_per_word = 12; pow(2, 12) == 4096
    _bytes = urandom(2 * n)   # only needs 1.5 bytes, but 2 is easier to work on
    shorts = (_bytes[(2 * i):(2 * i) + 2] for i in range(len(_bytes) / 2))
    for short in shorts:
        bits = ''.join(format(ord(short[i]), 'b').zfill(8) for i in range(2))
        index = 0;  offset = length / 2;
        for bit in (int(bit) for bit in bits):
            #assert isinstance(bit, int)
            if bit:
                index += offset
            offset /= 2
            if not offset:
                break
        output.append(_list[index])
    assert(len(output) == n)
    return output

def generate_phrase(length, _list=WORDLIST):
    """ usage: generate_phrase(length, list) => string

        Generates a random sequence of elements from _list.
        _list must be suitable for use as determined by `check_list`.
        The output is of the form

            entry0 entry1 entry2

        i.e. a string of words separated by spaces. """
    _size = len(_list)
    return ' '.join(sample(_list, length))

def test_generation(_list=WORDLIST):
    print("total number of words: {}".format(len(_list)))
    while True:
        phrase = generate_phrase(10)
        print(len(phrase.split(' ')), phrase)
        raw_input()

def test_sample():
    # TODO: proper statistical testing
    _list = range(4096)
    while True:
        samples = sample(_list, 4096)
        print(len(set(samples)))
        #print(len([x for x in _list if not samples.count(x)]))
        raw_input()

if __name__ == "__main__":
    #test_sample()
    test_generation()
