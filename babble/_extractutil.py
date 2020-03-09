FILENAMES = ("adjectives.txt", "adverbs.txt", "alliterations.txt",
             "compoundwords.txt", "conjunctions.txt",# "duos.txt",
             "interjections.txt", "nouns.txt", "occupations.txt",
             "pronouns.txt", "verbs.txt")

def _extract_words_from_raw_data(filenames=FILENAMES):
    """ usage: _extract_words_from_raw_data(filenames=FILENAMES) => None

        Parse the raw files and extract suitable entries.
        Hard coded to work with the files present in ./raw/
            - Have to roll your own if you want to parse other raw sources. """
    wordlist = []
    for filename in filenames:
        with open("./raw/" + filename, "r") as _file:
            data = _file.read()
        data = data.replace("<div class=wordlist-item>", '')
        data = data.replace("</div>", '\n').split('\n')
        # remove non-words, empty lines, duplicates
        # only take the first word from entries with spaces
        # WARNING:
        # failing to remove/truncate the entries with spaces could result in
        # easily guessable pass phrases when used with the shortcut solution.
        # e.g. `H(shortcut).update(last_n_words)`
        # if the last few entries are all multi-word entries, then the
        # last_n_words is less than n entries worth of information
        data = [word.split(' ')[0] for word in data if
                ("<div" not in word) and word.strip()]
        wordlist.extend(set(data))
    data = '\n'.join(wordlist)
    with open("wordlist.txt", 'w') as _file:
        _file.truncate(0)
        _file.write(data)
        _file.flush()

if __name__ == "__main__":
    _extract_words_from_raw_data()
