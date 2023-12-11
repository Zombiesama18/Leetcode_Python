import random, datetime

# 354. 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式(w, h)出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 说明:
# 不允许旋转信封。
List = []
for i in range(10000):
    List.append([random.randint(1, 10000), random.randint(1, 10000)])


def maxEnvelopes_recommended(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


start_time = datetime.datetime.now()
maxEnvelopes_recommended(List)
end_time = datetime.datetime.now()
print(end_time - start_time)
