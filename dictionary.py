class Dictionary(object):
    def __init__(self, dictionaryFile):
        self.dictionary = set()
        with open(dictionaryFile) as f:
            for word in f:
                self.dictionary.add(word.strip())

    def is_word(self, word):
        return word in self.dictionary
