# 연결 리스트를 이용해 실제 스택을 구현해보자

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next  # 이게 지금 바꾸는 거지,
        print(self.last.item)
        return item


stack = Stack()
print(stack.last)
stack.push(5)
stack.push(4)
stack.push(3)
print(stack.last.item)
print(stack.pop())
