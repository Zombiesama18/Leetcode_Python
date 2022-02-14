# 208. 实现 Trie (前缀树)
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
class Trie:
    class Node:
        def __init__(self, value='', isKey=False):
            self.value = value
            self.isKey = isKey
            self.map = {}
            self.numWords = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        self.size = 0

    def __len__(self):
        return self.getSize()

    def __subStartWith(self, x: Node, word: str, depth: int):
        if not x:
            return None
        if depth == len(word):
            return x
        char = word[depth]
        return self.__subStartWith(x.map.get(char), word, depth + 1)

    def __get(self, x: Node, word: str, depth: int):
        if not x:
            return None
        if depth == len(word):
            if x.isKey:
                return x
            else:
                return None
        char = word[depth]
        return self.__get(x.map.get(char), word, depth + 1)

    def __subTraverse(self, x: Node, result: str, keys: list):
        for char in x.map.keys():
            self.__subTraverse(x.map.get(char), result + char, keys)
        if x.isKey:
            keys.append(result)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for char in word:
            current.numWords += 1
            if not current.map.get(char):
                current.map[char] = self.Node(char, False)
            current = current.map.get(char)
        current.isKey = True
        self.size += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return bool(self.__get(self.root, word, 0))

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        x = self.__subStartWith(self.root, prefix, 0)
        return bool(x)

    def getSize(self):
        return self.size

    def clear(self):
        self.root = self.Node()
        self.size = 0

    def keysWithPerfix(self, perfix: str):
        x = self.__subStartWith(self.root, perfix, 0)
        if x:
            keys = []
            self.__subTraverse(x, perfix, keys)
            return keys
        return False


trie = Trie()
trie.insert('apple')
trie.search('apple')
trie.search('app')
trie.startsWith('app')
trie.insert('app')
trie.search('app')
