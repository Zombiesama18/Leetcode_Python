# 341. 扁平化嵌套列表迭代器（需要复习）
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
class NestedInteger:

    def isInteger(self):
        pass

    def getInterger(self):
        pass

    def getList(self):
        pass


class NestedIterator_withIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.result = list()
        self.dfs(self.nestedList.getList())
        self.iterator = self.result.__iter__()
        self.output = int

    def dfs(self, nestList):
        for nest in nestList:
            if nest.isInteger():
                self.result.append(nest)
            else:
                self.dfs(nest.getList())

    def next(self):
        return self.output

    def hasNext(self):
        try:
            self.output = self.iterator.__next__()
        except StopIteration:
            return False
        else:
            return True


class NestedIterator_withIndex:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.result = list()
        self.dfs(self.nestedList)
        self.index = 0
        self.length = len(self.result)

    def dfs(self, nestList):
        for nest in nestList:
            if nest.isInteger():
                self.result.append(nest)
            else:
                self.dfs(nest.getList())

    def next(self):
        temp = self.result[self.index]
        self.index += 1
        return temp

    def hasNext(self):
        return self.index < self.length
