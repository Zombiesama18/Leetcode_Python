"""
1093. 大样本统计

我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 在样本中出现的次数。
计算以下统计数据:
minimum ：样本中的最小元素。
maximum ：样品中的最大元素。
mean ：样本的平均值，计算为所有元素的总和除以元素总数。
median ：
如果样本的元素个数是奇数，那么一旦样本排序后，中位数 median 就是中间的元素。
如果样本中有偶数个元素，那么中位数median 就是样本排序后中间两个元素的平均值。
mode ：样本中出现次数最多的数字。保众数是 唯一 的。
以浮点数数组的形式返回样本的统计信息 [minimum, maximum, mean, median, mode] 。与真实答案误差在 10-5 内的答案都可以通过。
"""
import collections
from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        summation = 0
        max_num, min_num = 0, float('inf')
        mode, mode_num = 0, 0
        counter = 0
        nums, nums_counter = [], []
        for i, num in enumerate(count):
            if num == 0:
                continue
            max_num = max(max_num, i)
            min_num = min(min_num, i)
            if num > mode_num:
                mode_num = num
                mode = i
            summation += i * num
            counter += num
            nums.append(i)
        if counter % 2 != 0:
            target = counter // 2 + 1
        else:
            target = (counter // 2, counter // 2 + 1)
        median = self.median_helper(count, nums, target, 0, 0)
        return [float(min_num), float(max_num), summation / counter, float(median), float(mode)]

    def median_helper(self, count, nums, target, current_idx, current_counter):
        if isinstance(target, int):
            if current_counter + count[nums[current_idx]] >= target:
                return nums[current_idx]
            else:
                return self.median_helper(count, nums, target, current_idx + 1, current_counter + count[nums[current_idx]])
        else:
            if current_counter + count[nums[current_idx]] >= target[1]:
                return nums[current_idx]
            elif current_counter + count[nums[current_idx]] >= target[0]:
                return (nums[current_idx] + self.median_helper(count, nums, target, current_idx + 1, current_counter +
                                                               count[nums[current_idx]])) / 2
            else:
                return self.median_helper(count, nums, target, current_idx + 1, current_counter +
                                          count[nums[current_idx]])


Solution().sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
