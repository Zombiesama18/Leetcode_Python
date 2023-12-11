"""
《炸金花》底层逻辑实现
自己写一个程序，实现发牌、比大小判断输赢
游戏规则:
一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢.
有以下几种牌:
豹子:三张一样的牌，如3张6.如红桃5、6、7同花顺: 即3张同样花色的顺子
顺子:又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子对子: 2张牌一样单张: 单张最大的是A这几种牌的大小顺序为， 豹子>同花顺>同花>顺子>对子>单张
需程序实现的点:
1.先生成一付完整的扑克牌
2.给5个玩家随机发牌
3.统一开牌，比大小，输出赢家是谁
"""
import collections
import itertools
import random

id2color = {0: '方片', 1: '红桃', 2: '黑桃', 3: '梅花'}

id2card = dict(zip(list(range(2, 10)), list(map(chr, list(range(ord('0') + 2, ord('0') + 10))))))
id2card[10] = '10'
id2card[11] = 'J'
id2card[12] = 'Q'
id2card[13] = 'K'
id2card[14] = 'A'


def translate_to_poker(inputs: tuple):
    return ' '.join([id2color[inputs[0]], id2card[inputs[1]]])

def calculate_points(colors: list, cards: list):
    if all(cards[i] == cards[0] for i in range(len(cards))):
        return 6
    cards.sort()
    if all(colors[i] == colors[0] for i in range(len(colors))) and all(cards[i + 1] - cards[i] == 1 for i in range(len(cards) - 1)):
        return 5
    if all(colors[i] == colors[0] for i in range(len(colors))):
        return 4
    if all(cards[i + 1] - cards[i] == 1 for i in range(len(cards) - 1)):
        return 3
    if any(num1 == num2 for num1, num2 in itertools.combinations(cards, 2)):
        return 2
    return 1

def check_baozi(inputs: list):
    initial_card = inputs[0][1]
    for color, card in inputs:
        if card != initial_card:
            return False
    return True

def func():
    # 初始设置
    players = 5
    cards_in_hand = 3
    cards = [(x, y) for x in range(4) for y in range(2, 15)]
    random.shuffle(cards)
    players_cards = [[] for _ in range(players)]

    # 发牌过程
    index = 0
    counter = 0
    while counter < players * cards_in_hand:
        players_cards[index % players].append(cards.pop(0))
        index += 1
        counter += 1

    for i in range(players):
        print(f'玩家{i}的手牌为：', ' '.join(list(translate_to_poker(card).ljust(6) for card in players_cards[i])))
    # 计分过程
    points = [0 for _ in range(5)]
    for i, card in enumerate(players_cards):
        points[i] = calculate_points([card[i][0] for i in range(len(card))], [card[j][1] for j in range(len(card))])
    max_point = max(points)
    winners = []
    for i, point in points:
        if point == max_point:
            winners.append(i)

    # 如果有同分
    if len(winners) > 1:
        second_round = []
        for winner in winners:
            second_round.append([players_cards[winner][i][1] for i in range(cards_in_hand)])
        if max_point == 2:
            for i, cards in enumerate(second_round):
                cards = collections.Counter(cards)
                for key, value in cards.items():
                    if value == 2:
                        second_round[i] = [key]


if __name__ == '__main__':
    func()

