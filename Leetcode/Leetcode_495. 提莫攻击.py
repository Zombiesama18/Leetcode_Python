# 495. 提莫攻击
# 在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄。他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。
# 当提莫攻击艾希，艾希的中毒状态正好持续 duration 秒。
# 正式地讲，提莫在 t 发起发起攻击意味着艾希在时间区间 [t, t + duration - 1]（含 t 和 t + duration - 1）处于中毒状态。
# 如果提莫在中毒影响结束 前 再次攻击，中毒状态计时器将会 重置 ，在新的攻击之后，中毒影响将会在 duration 秒后结束。
# 给你一个 非递减 的整数数组 timeSeries ，其中 timeSeries[i] 表示提莫在 timeSeries[i] 秒时对艾希发起攻击，
# 以及一个表示中毒持续时间的整数 duration 。
# 返回艾希处于中毒状态的 总 秒数。
def findPoisonedDuration(timeSeries: [int], duration: int) -> int:
    result = 0
    end_time = float('-INF')
    for start_time in timeSeries:
        if start_time <= end_time:
            result += duration + start_time - end_time
        else:
            result += duration
        end_time = start_time + duration
    return result




