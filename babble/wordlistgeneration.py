import string
import base64

import babble.profanity

def generate_wordlist_from(filename, letters=string.letters,
                           profanity_filter=babble.profanity.FILTER):
    wordlist = []
    encode = base64.standard_b64encode
    with open(filename, 'r') as _file:
        for line in _file.readlines():
            wordlist.extend(word.strip().lower() for word in line.split(' ') if
                            (not set(word).difference(letters)) and
                            word and
                           encode(word.strip().lower()) not in profanity_filter)
    return list(sorted(set(wordlist), key=len)) # set removes duplicates

def main():
    filename = "/home/e/Downloads/bookofshadows/podsbos7.txt"
    wordlist = generate_wordlist_from(filename)
    with open("wordlist.py", "w") as _file:
        _file.write("WORDLIST =\\\n")
        _file.write('(')
        _file.write('\n'.join("'{}',".format(word) for word in wordlist[:4096]))
        _file.write(')')
        _file.flush()

if __name__ == "__main__":
    main()
