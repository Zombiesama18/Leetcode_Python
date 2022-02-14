# 706. 设计哈希映射
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 13
        self.map = [None for _ in range(self.base)]
        self.keys = list()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = key % self.base
        if self.map[hashcode] is None:
            self.map[hashcode] = [Entry(key, value)]
            self.keys.append(key)
        elif key in self.keys:
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    subEntry.value = value
        else:
            self.map[hashcode].append(Entry(key, value))
            self.keys.append(key)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = key % self.base
        if self.map[hashcode]:
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    return subEntry.value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            hashcode = key % self.base
            for subEntry in self.map[hashcode]:
                if subEntry.key == key:
                    self.map[hashcode].remove(subEntry)
            self.keys.remove(key)


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.get(1)
myHashMap.get(3)
myHashMap.put(2, 1)
myHashMap.get(2)
myHashMap.remove(2)
myHashMap.get(2)

