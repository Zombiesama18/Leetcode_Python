# 211. 添加与搜索单词 - 数据结构设计
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 实现词典类 WordDictionary ：
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
class WordDictionary:
    class Node:
        def __init__(self, value: str, isKey: bool):
            self.value = value
            self.children = {}
            self.isKey = isKey

    def __init__(self):
        self.root = self.Node('', False)

    def addWord(self, word: str) -> None:
        self.addWordHelper(self.root, word, 0)
        return

    def addWordHelper(self, node: Node, word: str, index: int):
        if index == len(word):
            node.isKey = True
            return
        if word[index] not in node.children:
            node.children[word[index]] = self.Node(word[index], False)
        self.addWordHelper(node.children[word[index]], word, index + 1)
        return

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word, 0)

    def searchHelper(self, node: Node, word: str, index: int):
        if index == len(word):
            return node.isKey
        if word[index] == '.':
            flag = False
            for child in node.children:
                flag = flag or self.searchHelper(node.children[child], word, index + 1)
                if flag:
                    return True
        else:
            if word[index] not in node.children:
                return False
            else:
                return self.searchHelper(node.children[word[index]], word, index + 1)
        return False


wd = WordDictionary()
wd.addWord('bad')
wd.addWord('dad')
wd.addWord('mad')
wd.search('pad')
wd.search('bad')
wd.search('.ad')
wd.search('b..')

