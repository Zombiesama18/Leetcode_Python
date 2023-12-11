# 2043. 简易银行系统
# 你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 n 个账户，编号从 1 到 n 。
# 每个账号的初始余额存储在一个下标从 0 开始的整数数组 balance  中，其中第 (i + 1) 个账户的初始余额是 balance[i] 。
# 请你执行所有 有效的 交易。如果满足下面全部条件，则交易 有效 ：
# 指定的账户数量在 1 和 n 之间，且
# 取款或者转账需要的钱的总数 小于或者等于 账户余额。
# 实现 Bank 类：
# Bank(long[] balance) 使用下标从 0 开始的整数数组 balance 初始化该对象。
# boolean transfer(int account1, int account2, long money) 从编号为  account1 的账户向编号为 account2 的账户转帐 money 美元。
# 如果交易成功，返回 true ，否则，返回 false 。
# boolean deposit(int account, long money) 向编号为  account 的账户存款 money 美元。如果交易成功，返回 true ；否则，返回 false 。
# boolean withdraw(int account, long money) 从编号为 account 的账户取款 money 美元。如果交易成功，返回 true ；否则，返回 false 。
class Bank:

    def __init__(self, balance: [int]):
        self.balance = [0]
        self.balance.extend(balance)
        self.balanceNumber = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.balanceNumber or account2 > self.balanceNumber or self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.balanceNumber:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.balanceNumber or self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True


bank = Bank([10, 100, 20, 50, 30])
bank.withdraw(3, 10)
bank.transfer(5, 1, 20)
bank.deposit(5, 20)
bank.transfer(3, 4, 15)
bank.withdraw(10, 50)
