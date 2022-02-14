# 447. 回旋镖的数量
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，
# 其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
# 返回平面上所有回旋镖的数量。
def numberOfBoomerangs(points: [[int]]) -> int:
    length = len(points)
    if length < 3:
        return 0
    result = 0
    for point1 in points:
        distanceDict = {}
        for point2 in points:
            distance = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
            distanceDict[distance] = distanceDict.setdefault(distance, 0) + 1
        for m in distanceDict.values():
            result += m * (m - 1)
    return result




