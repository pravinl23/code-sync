class Trie(object):

    def __init__(self):
        self.trie = {} 

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            # move forward into the trie
            d = d[c]
        d['.'] = '.'

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]

        return '.' in d

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)