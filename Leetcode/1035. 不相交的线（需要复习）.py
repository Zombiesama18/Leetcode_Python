# 1035. 不相交的线（需要复习）
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：
# nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
# 以这种方法绘制线条，并返回可以绘制的最大连线数。

# 最长公共子序列
def maxUncrossedLines(nums1: [int], nums2: [int]) -> int:
    columns = len(nums1)
    rows = len(nums2)
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if nums2[i - 1] == nums1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


maxUncrossedLines([1,4,2], [1,2,4])
maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])
maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])
