# 1006. 笨阶乘
# 通常，正整数 n1 的阶乘是所有小于或等于 n1 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：
# 我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
# 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
def clumsy(N: int):
    operator = ['*', '/', '+', '-']
    operatorCounter = 0
    numStack = [N]
    numCounter = N - 1
    firstSet = True

    def operate(currentOperator):
        if currentOperator == '*':
            operateLatterNum = numStack.pop(-1)
            numStack.append(operateLatterNum * numStack.pop(-1))
        elif currentOperator == '/':
            operateLatterNum = numStack.pop(-1)
            numStack.append(int(numStack.pop(-1) / operateLatterNum))
        elif currentOperator == '+':
            if firstSet:
                operateLatterNum = numStack.pop(-1)
                numStack.append(numStack.pop(-1) + operateLatterNum)
            else:
                operateLatterNum = numStack.pop(-1)
                numStack.append(numStack.pop(-1) - operateLatterNum)
        else:
            operateLatterNum = numStack.pop(-1)
            numStack.append(numStack.pop(-1) - operateLatterNum)

    while numCounter > 0:
        currentOperator = operator[operatorCounter % 4]
        operatorCounter += 1
        numStack.append(numCounter)
        numCounter -= 1
        if currentOperator != '-':
            operate(currentOperator)
        else:
            firstSet = False
    for i in range(len(numStack)):
        if i != 0:
            numStack[i] = -numStack[i]
    return sum(numStack)


clumsy(4)


def clumsyVersion2(N: int):
    firstSet = True
    setNumber = N >> 2
    remainder = N % 4
    finalSetIfFirstSet = [0, 1, 2 * 1, int(3 * 2 / 1)]
    finalSetIfNotFirstSet = [0, - 1, - 2 * 1, -int(3 * 2 / 1)]
    result = []
    for i in range(setNumber):
        if firstSet:
            firstSet = False
            result.append(int(N * (N - 1) / (N - 2)) + N - 3)
        else:
            result.append(-int(N * (N - 1) / (N - 2)) + N - 3)
        N -= 4
    if firstSet:
        result.append(finalSetIfFirstSet[remainder])
    else:
        result.append(finalSetIfNotFirstSet[remainder])
    return sum(result)


clumsyVersion2(10)
