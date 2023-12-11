# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。


def sortColors(nums):
    output = []
    index_white = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            output.insert(0, 0)
            index_white = index_white + 1
        elif nums[i] == 1:
            output.insert(index_white, 1)
        elif nums[i] == 2:
            output.insert(-1, 2)
        else:
            print('出现了其他颜色，不计入统计')
    print(output)


sortColors([2, 0, 2, 1, 1, 0])
