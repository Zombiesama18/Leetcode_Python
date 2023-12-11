# 877. 石子游戏
# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
# 游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
# 亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
# 假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
def stoneGame(piles: [int]) -> bool:
    alexAndLee = [0, 0]
    leeTurn = False
    while piles:
        if leeTurn:
            smaller = min(piles[0], piles[-1])
            index = 0 if piles[0] < piles[-1] else -1
            alexAndLee[int(leeTurn)] += smaller
            piles.pop(index)
        else:
            bigger = max(piles[0], piles[-1])
            index = 0 if piles[0] > piles[-1] else -1
            alexAndLee[int(leeTurn)] += bigger
            piles.pop(index)
        leeTurn = not leeTurn
    return alexAndLee[0] > alexAndLee[1]




