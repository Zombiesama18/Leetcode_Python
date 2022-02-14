# 17. 电话号码的字母组合（需要复习）
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 不定长的循环就用递归
# 可以使用函数中的函数


def letterCombinations(digits):
    letter_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    output = []

    def recursion(comb, nextdigits):
        if not nextdigits:
            output.append(comb)
        else:
            for i in letter_dict[nextdigits[0]]:
                recursion(comb + i, nextdigits[1:])

    recursion('', digits)
    if output[0] == '':
        return []
    return output


digitsList = ['23', '', '2']
for i in range(len(digitsList)):
    print('输入：{}\t结果：{}'.format(digitsList[i], letterCombinations(digitsList[i])))


def letterCombinationsFaster(digits):
    if not digits:
        return list()
    letter_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []

    def combinationHelper(combination: str, word: str, depth: int):
        if depth == len(word):
            result.append(combination)
            return
        for char in letter_dict[word[depth]]:
            combinationHelper(combination + char, word, depth + 1)

    combinationHelper('', digits, 0)
    return result




