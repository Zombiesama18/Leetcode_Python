# 401. 二进制手表
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。
# 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。
# 小时不会以零开头：
# 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
# 分钟必须由两位数组成，可能会以零开头：
# 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
def readBinaryWatch(turnedOn: int) -> [str]:
    if turnedOn > 8:
        return []
    result = []
    for hour in range(12):
        for minute in range(60):
            if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                result.append('{}:{}'.format(str(hour), str(minute).zfill(2)))
    return result




