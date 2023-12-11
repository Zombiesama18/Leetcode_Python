"""
年会抽奖
路飞科技有限公司有300员工，开年会抽奖，奖项如下:
一等奖 3名:泰国5日游+手术费报销
二等奖6名:iPhone14手机
三等奖30名:三斤苹果
规则:
1.共抽3次，第一次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖2.每个员工限中奖一次，不能重复
解题思路:
1.生成一个员工列表，用random模块从里面取随机值2.取完值之后，立刻从员工大列表里把中奖人删掉，即可防止其再次中奖
"""
import random


def func():
    employee = set(range(0, 300))
    print(f'员工代号为：{employee}')
    for i in [1, 2, 3]:
        if i == 1:
            winner = random.sample(list(employee), k=30)
            print(f'获得三等奖的员工代号:{winner}')
        elif i == 2:
            winner = random.sample(list(employee), k=6)
            print(f'获得二等奖的员工代号:{winner}')
        elif i == 3:
            winner = random.sample(list(employee), k=3)
            print(f'获得一等奖的员工代号:{winner}')
        for p in winner:
            employee.remove(p)
    return


if __name__ == '__main__':
    func()


