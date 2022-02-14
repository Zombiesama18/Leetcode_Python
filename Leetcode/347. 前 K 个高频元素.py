# 347. 前 K 个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
def topKFrequent(nums, k):
    temp = set(nums)
    temp_dict = {}
    for i in temp:
        times = nums.count(i)
        if times in temp_dict:
            temp_value = [temp_dict[times], i]
            temp_dict[times] = temp_value
        else:
            temp_dict[times] = i
    frequence = list(temp_dict.keys())
    frequence.sort()
    frequence.reverse()
    output = []
    for i in range(k):
        output.append(temp_dict[frequence[i]])
    return output


nums = [1, 1, 1, 2, 2, 3, 3]
k = 2
topKFrequent(nums, k)
