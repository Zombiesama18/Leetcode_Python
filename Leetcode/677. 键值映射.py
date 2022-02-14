# 677. 键值映射
# 实现一个 MapSum 类，支持两个方法，insert 和 sum：
# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，
# 那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
class MapSum:
    class Node:
        def __init__(self):
            self.children = [0 for _ in range(26)]
            self.is_key = False
            self.value = 0

    def __init__(self):
        self.sum_result = 0
        self.root = self.Node()
        self.base = ord('a')

    def insert(self, key: str, val: int) -> None:
        self.insert_helper(self.root, key, val, 0)

    def insert_helper(self, node, key, val, index):
        if index == len(key):
            node.is_key = True
            node.value = val
            return
        if node.children[ord(key[index]) - self.base] == 0:
            node.children[ord(key[index]) - self.base] = self.Node()
        self.insert_helper(node.children[ord(key[index]) - self.base], key, val, index + 1)

    def sum(self, prefix: str) -> int:
        self.sum_result = 0
        located_node = self.locate_node(self.root, prefix, 0)
        if not located_node:
            return 0
        self.sum_helper(located_node)
        return self.sum_result

    def locate_node(self, node, prefix, index):
        if index == len(prefix):
            return node
        if node.children[ord(prefix[index]) - self.base] == 0:
            return None
        return self.locate_node(node.children[ord(prefix[index]) - self.base], prefix, index + 1)

    def sum_helper(self, node):
        if node.is_key:
            self.sum_result += node.value
        for child in node.children:
            if child != 0:
                self.sum_helper(child)


mapSum = MapSum()
mapSum.insert('apple', 3)
mapSum.sum('ap')
mapSum.insert('app', 2)
mapSum.sum('ap')



