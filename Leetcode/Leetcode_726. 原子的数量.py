# 726. 原子的数量
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
# 两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
# 给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），
# 跟着它的数量（如果数量大于 1），以此类推。
def countOfAtoms(formula: str) -> str:
    states = ['ELEMENT', 'DIGIT', 'BRACKET']
    elementDict = {}
    currentState = 'ELEMENT'
    stateStack = []
    numberStack = []
    tempChar = []
    tempNumber = ''
    formula = list(formula)
    formula.append('END')
    for char in formula:
        if char.isalpha():
            if currentState == 'DIGIT':
                currentState = 'ELEMENT'
                numberStack.append(int(tempNumber))
            elif currentState == 'ELEMENT':
                numberStack.append(1)
            elif currentState == 'BRACKET':
                while tempChar[-1] != '(':

            if char.isupper():
                tempChar.append(char)
            else:
                tempChar[-1] += char
        elif char.isdigit():
            if currentState == 'ELEMENT':
                tempElement = tempChar.pop(-1)
                elementDict[tempElement] = elementDict.setdefault(tempElement, 0) + numberStack.pop(-1)






