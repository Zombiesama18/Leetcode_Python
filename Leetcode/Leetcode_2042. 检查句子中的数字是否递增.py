# 2042. 检查句子中的数字是否递增
# 句子是由若干 token 组成的一个列表，token 间用 单个 空格分隔，句子没有前导或尾随空格。
# 每个 token 要么是一个由数字 0-9 组成的不含前导零的 正整数 ，要么是一个由小写英文字母组成的 单词 。
# 示例，"a puppy has 2 eyes 4 legs" 是一个由 7 个 token 组成的句子："2" 和 "4" 是数字，其他像 "puppy" 这样的 tokens 属于单词。
# 给你一个表示句子的字符串 s ，你需要检查 s 中的 全部 数字是否从左到右严格递增（即，除了最后一个数字，s 中的 每个 数字都严格小于它 右侧 的数字）。
# 如果满足题目要求，返回 true ，否则，返回 false 。
def areNumbersAscending(s: str) -> bool:
    lastNumber = -1
    index = 0
    length = len(s)
    while index < length:
        if not s[index].isdigit():
            index += 1
            continue
        currentNumber = 0
        while index < length and s[index].isdigit():
            currentNumber = 10 * currentNumber + int(s[index])
            index += 1
        if currentNumber <= lastNumber:
            return False
        lastNumber = currentNumber
    return True


areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
areNumbersAscending("hello world 5 x 5")
areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")

