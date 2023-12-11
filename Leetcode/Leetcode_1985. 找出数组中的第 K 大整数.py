# 1985. 找出数组中的第 K 大整数
# 给你一个字符串数组 nums 和一个整数 k 。nums 中的每个字符串都表示一个不含前导零的整数。
# 返回 nums 中表示第 k 大整数的字符串。
# 注意：重复的数字在统计时会视为不同元素考虑。例如，如果 nums 是 ["1","2","2"]，那么 "2" 是最大的整数，
# "2" 是第二大的整数，"1" 是第三大的整数。
def kthLargestNumber(nums: [str], k: int) -> str:
    numDict = {}
    for num in nums:
        numDict[int(num)] = numDict.setdefault(int(num), 0) + 1
    nums = list(numDict.keys())
    nums.sort(reverse=True)
    index = 0
    while k - numDict[nums[index]] > 0:
        k -= numDict[nums[index]]
        index += 1
    return str(nums[index])


kthLargestNumber(["3","6","7","10"], 4)
kthLargestNumber( ["2","21","12","1"], 3)
kthLargestNumber(["0","0"], 2)


def kthLargestNumberVersion2(nums: [str], k: int) -> str:
    nums.sort(key=lambda x: int(x), reverse=True)
    return nums[k - 1]


kthLargestNumberVersion2(["3","6","7","10"], 4)
kthLargestNumberVersion2( ["2","21","12","1"], 3)
kthLargestNumberVersion2(["0","0"], 2)

