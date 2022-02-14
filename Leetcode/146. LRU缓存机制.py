# 146. LRU缓存机制
# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
# 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.inner_dict = {}

    def get(self, key):
        if key in self.inner_dict.keys():
            value = self.inner_dict.pop(key)
            self.inner_dict[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if len(self.inner_dict) == self.capacity:
            self.inner_dict.pop(list(self.inner_dict.keys())[0])
        self.inner_dict[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
