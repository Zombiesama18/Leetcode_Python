# 155. 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
class MinStack:

    def __init__(self):
        self.values = []

    def push(self, x):
        self.values.append(x)

    def pop(self):
        self.values.pop(-1)

    def top(self):
        return self.values[-1]

    def getMin(self):
        return min(self.values)


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
