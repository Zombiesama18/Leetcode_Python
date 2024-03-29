# 502. IPO
# 假设 力扣（LeetCode）即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。
# 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
# 给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。最初，你有 W 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
# 总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。
import heapq


def findMaximizedCapital(k: int, w: int, profits: [int], capital: [int]) -> int:
    if w > max(capital):
        return w + sum(heapq.nlargest(k, profits))
    length = len(profits)
    arr = [(profits[i], capital[i]) for i in range(length)]
    pq = []
    arr.sort(key=lambda x: x[1])
    currentIndex = 0
    for _ in range(k):
        while currentIndex < length and arr[currentIndex][1] <= w:
            heapq.heappush(pq, -arr[currentIndex][0])
            currentIndex += 1
        if pq:
            w -= heapq.heappop(pq)
        else:
            break
    return w






