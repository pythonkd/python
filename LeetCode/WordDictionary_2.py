class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        l = len(word)
        if l not in self.di:
            self.di[l] = [word]
        else:
            self.di[l].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        l = len(word)

        if l not in self.di:
            return False
        if '.' not in word:
            return word in self.di[l]

        for words in self.di[l]:
            for j in range(l):

                if word[j] != '.' and word[j] != words[j]:

                    break
                elif j == l - 1:
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
if __name__ == '__main__':
    t = WordDictionary()
    t.addWord("add")
    t.addWord("tdd")
    t.addWord("serc")
    t.search("..e")