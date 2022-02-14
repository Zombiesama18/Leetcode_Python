class List:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self, nodeValues):
        self.head = self.generateListNode(nodeValues)

    def generateListNode(self, nodeValues: list):
        l1 = self.ListNode(nodeValues.pop(0))
        head = l1
        while nodeValues:
            head.next = self.ListNode(nodeValues.pop(0))
            head = head.next
        return l1

    def traverseListNode(self):
        temp = self.head
        while temp:
            print(temp.val, end='->')
            temp = temp.next
