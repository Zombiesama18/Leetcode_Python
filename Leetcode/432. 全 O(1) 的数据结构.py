"""
432. 全 O(1) 的数据结构
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
实现 AllOne 类：
AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。
测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
"""
import collections


class BidirectionalNode:
    def __init__(self, key='', count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node):
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:

    def __init__(self):
        self.root = BidirectionalNode()
        self.root.prev = self.root
        self.root.next = self.root
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(BidirectionalNode(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            current = self.nodes[key]
            nextNode = current.next
            if nextNode is self.root or nextNode.count > current.count + 1:
                self.nodes[key] = current.insert(BidirectionalNode(key, current.count + 1))
            else:
                nextNode.keys.add(key)
                self.nodes[key] = nextNode
            current.keys.remove(key)
            if len(current.keys) == 0:
                current.remove()

    def dec(self, key: str) -> None:
        current = self.nodes[key]
        if current.count == 1:
            del self.nodes[key]
        else:
            preNode = current.prev
            if preNode is self.root or preNode.count < current.count - 1:
                self.nodes[key] = current.prev.insert(BidirectionalNode(key, current.count - 1))
            else:
                preNode.keys.add(key)
                self.nodes[key] = preNode
        current.keys.remove(key)
        if len(current.keys) == 0:
            current.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ''

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ''
