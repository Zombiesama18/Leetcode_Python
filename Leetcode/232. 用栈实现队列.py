# 232. 用栈实现队列
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
# 你只能使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.reverse = False
        self.size = 0

    def push(self, x):
        if self.reverse:
            for i in range(self.size):
                self.stack1.append(self.stack2.pop())
            self.reverse = False
        self.stack1.append(x)
        self.size += 1

    def pop(self):
        if not self.reverse:
            for i in range(self.size):
                self.stack2.append(self.stack1.pop())
            self.reverse = True
        self.size -= 1
        return self.stack2.pop()

    def peek(self):
        if not self.reverse:
            for i in range(self.size):
                self.stack2.append(self.stack1.pop())
            self.reverse = True
        return self.stack2[-1]

    def empty(self):
        return self.size == 0


myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
myqueue.peek()
myqueue.pop()
myqueue.empty()
