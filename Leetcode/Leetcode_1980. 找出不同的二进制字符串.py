# 1980. 找出不同的二进制字符串
# 给你一个字符串数组 nums ，该数组由 n 个 互不相同 的二进制字符串组成，且每个字符串长度都是 n 。
# 请你找出并返回一个长度为 n 且 没有出现 在 nums 中的二进制字符串。如果存在多种答案，只需返回 任意一个 即可。
def findDifferentBinaryString(nums: [str]) -> str:
    length = len(nums)
    values = {int(num, 2) for num in nums}
    counter = 0
    while counter in values:
        counter += 1
    return bin(counter)[2:].zfill(length)


