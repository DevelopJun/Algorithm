# 큐를 스택으로 구현 해봄.

from typing import Collection


class Queue:

    def __init__(self):
        from collections import deque
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        # 요소 삽입 후 맨 앞에 두는 상태로 재 정렬(이거는 왜 하는지 모르겠음.)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


Queue = Queue()
Queue.push(5)
print(Queue.q)
Queue.push(6)
print(Queue.q)
