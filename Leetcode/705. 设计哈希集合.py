# 705. 设计哈希集合
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
class MyHashSet:
    def __init__(self):
        self.dict = {}
        self.base = 13

    def add(self, key: int):
        hashcode = key % self.base
        if not self.dict.get(hashcode):
            self.dict[hashcode] = [key]
        else:
            if key not in self.dict[hashcode]:
                self.dict[hashcode].append(key)
        return

    def remove(self, key: int):
        hashcode = key % self.base
        if hashcode in self.dict.keys():
            if key in self.dict[hashcode]:
                if len(self.dict[hashcode]) == 1:
                    self.dict.pop(hashcode)
                else:
                    self.dict[hashcode].remove(key)
        return

    def contains(self, key: int):
        hashcode = key % self.base
        if hashcode in self.dict.keys():
            if key in self.dict[hashcode]:
                return True
        return False


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1)
myHashSet.contains(3)
myHashSet.add(2)
myHashSet.contains(2)
myHashSet.remove(2)
myHashSet.contains(2)

