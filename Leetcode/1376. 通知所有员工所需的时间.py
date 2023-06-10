"""
1376. 通知所有员工所需的时间

公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。
在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。
题目保证从属关系可以用树结构显示。
公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，
直到所有的员工都得知这条紧急消息。
第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，
他的所有直属下属都可以开始传播这一消息）。
返回通知所有员工这一紧急消息所需要的 分钟数 。
"""
import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager) == 1:
            return 0
        result = 0
        queue = collections.deque([(headID, 0)])
        relation_dict = collections.defaultdict(list)
        for i, person in enumerate(manager):
            relation_dict[person].append(i)
        while queue:
            current_person, total_time = queue.popleft()
            result = max(result, total_time)
            for next_person in relation_dict[current_person]:
                queue.append((next_person, total_time + informTime[current_person]))
        return result


Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])
Solution().numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1])
