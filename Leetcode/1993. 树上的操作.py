# 1993. 树上的操作
# 给你一棵  n  个节点的树，编号从  0  到  n - 1  ，以父节点数组  parent  的形式给出，其中  parent[i]  是第  i  个节点的父节点。
# 树的根节点为 0  号节点，所以  parent[0] = -1  ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。
# 数据结构需要支持如下函数：
# Lock：指定用户给指定节点 上锁  ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。
# Unlock：指定用户给指定节点 解锁  ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。
# Upgrade：指定用户给指定节点  上锁  ，并且将该节点的所有子孙节点  解锁  。只有如下 3 个条件 全部 满足时才能执行升级操作：
# 指定节点当前状态为未上锁。
# 指定节点至少有一个上锁状态的子孙节点（可以是 任意  用户上锁的）。
# 指定节点没有任何上锁的祖先节点。
# 请你实现  LockingTree  类：
# LockingTree(int[] parent)  用父节点数组初始化数据结构。
# lock(int num, int user) 如果  id 为  user  的用户可以给节点  num  上锁，那么返回  true  ，否则返回  false  。
# 如果可以执行此操作，节点  num  会被 id 为 user  的用户 上锁  。
# unlock(int num, int user)  如果 id 为 user  的用户可以给节点 num  解锁，那么返回  true  ，否则返回 false  。
# 如果可以执行此操作，节点 num  变为 未上锁  状态。
# upgrade(int num, int user)  如果 id 为 user  的用户可以给节点 num  升级，那么返回  true  ，否则返回 false  。
# 如果可以执行此操作，节点 num  会被  升级 。
import collections


class LockingTreeAnother:

    def __init__(self, parent: [int]):
        self.parents = parent
        self.length = len(self.parents)
        self.children = collections.defaultdict(list)
        for i in range(1, self.length):
            self.children[parent[i]].append(i)
        self.lockState = [[False, None] for _ in range(self.length)]

    def lock(self, num: int, user: int) -> bool:
        if not self.lockState[num][0]:
            self.lockState[num][0] = True
            self.lockState[num][1] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lockState[num][1] == user:
            self.lockState[num][0] = False
            self.lockState[num][1] = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.lockState[num][0]:
            return False
        parent = self.parents[num]
        while parent != -1:
            if self.lockState[parent][0]:
                return False
            parent = self.parents[parent]
        stateFlag = False
        for child in self.children[num]:
            stateFlag = stateFlag or self.upgradeHelper1(child)
        if stateFlag:
            self.upgradeHelper2(num)
            self.lockState[num][0] = True
            self.lockState[num][1] = user
            return True
        return False

    def upgradeHelper1(self, currentNode: int):
        if self.lockState[currentNode][0]:
            return True
        for child in self.children[currentNode]:
            if self.upgradeHelper1(child):
                return True
        return False

    def upgradeHelper2(self, currentNode: int):
        self.lockState[currentNode][0] = False
        self.lockState[currentNode][1] = None
        for child in self.children[currentNode]:
            self.upgradeHelper2(child)


obj2 = LockingTreeAnother([-1, 0, 0, 1, 1, 2, 2])
obj2.lock(2, 2)
obj2.unlock(2, 3)
obj2.unlock(2, 2)
obj2.lock(4, 5)
obj2.upgrade(0, 1)
obj2.lock(0, 1)
