# 38. 外观数列
# 给定一个正整数 n ，输出外观数列的第 n 项。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
# 你可以将其视作是由递归公式定义的数字字符串序列：
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
# 前五项如下：
def countAndSay(n: int) -> str:
    lastResult = '1'
    if n == 1:
        return lastResult
    for i in range(2, n + 1):
        counter = 1
        lastDigit = lastResult[0]
        temp = ''
        for j in range(1, len(lastResult)):
            if lastResult[j] == lastDigit:
                counter += 1
            else:
                temp += str(counter)
                temp += lastDigit
                lastDigit = lastResult[j]
                counter = 1
        temp += str(counter)
        temp += lastResult[-1]
        lastResult = temp
    return lastResult


countAndSay(2)
countAndSay(3)
countAndSay(4)
countAndSay(5)
countAndSay(30)
