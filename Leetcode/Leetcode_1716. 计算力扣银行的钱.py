"""
1716. 计算力扣银行的钱
Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。
最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。
给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。
"""


def totalMoney(n: int) -> int:
    return n // 7 * 28 + (n // 7) * (n // 7 - 1) * 7 // 2 + n % 7 * (1 + n // 7) + n % 7 * (n % 7 - 1) // 2



