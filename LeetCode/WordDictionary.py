class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w in node.keys():
                node = node[w]
            else:
                node[w] = {}
                node = node[w]
        node['end'] = True

    def search(self, word, prevnode=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        #         if prevnode is None:
        node = self.root
        #         else:
        #             print('..')
        #             node = prevnode
        for w in word:
            if w == '.':
                return any([self.search(word.replace('.', i, 1)) for i in node.keys() if i != 'end'])
            else:
                if w not in node.keys():
                    return False
                else:
                    node = node[w]
        return node.get('end') is not None
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
if __name__ == '__main__':
    t = WordDictionary()
    t.addWord('bad')
    t.addWord('dad')
    t.addWord('mad')
    assert not t.search("pad")
    assert t.search("bad")
    t.search("b..")