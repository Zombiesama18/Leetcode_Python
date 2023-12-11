"""
2327. 知道秘密的人数
在第 1 天，有一个人发现了一个秘密。
给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 forget ，
表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。
给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 109 + 7 取余 后返回。
"""
import sortedcontainers


def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    delay_dict = sortedcontainers.SortedDict({delay + 1: 1})
    forget_dict = sortedcontainers.SortedDict({forget + 1: 1})
    current_broadcasting_number = 0
    days = 1
    BASE = 10 ** 9 + 7
    result = 1
    while days <= n:
        if delay_dict.items()[0][0] == days:
            current_broadcasting_number += delay_dict.items()[0][1]
            del delay_dict[delay_dict.items()[0][0]]
        if forget_dict.items()[0][0] == days:
            current_broadcasting_number -= forget_dict.items()[0][1]
            if result < forget_dict.items()[0][1]:
                result = BASE + result - forget_dict.items()[0][1]
            else:
                result -= forget_dict.items()[0][1]
            del forget_dict[forget_dict.items()[0][0]]
        result = (result + current_broadcasting_number) % BASE
        delay_dict[days + delay] = delay_dict.get(days + delay, 0) + current_broadcasting_number
        forget_dict[days + forget] = forget_dict.get(days + forget, 0) + current_broadcasting_number
        days += 1
    return result


peopleAwareOfSecret(n = 6, delay = 2, forget = 4)
peopleAwareOfSecret(4, 1, 4)
