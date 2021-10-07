# 입력 : ""
# 츨력 : ""
from collections import deque


class Stack:
    def dailyTemperature(self, list: list[int]) -> list[int]:
        temperature = list
        result = [0] * len(temperature)
        stack = []
        for i, cur in enumerate(temperature):
            print(i, cur)
            # 현재 온도가 스택 값 보다 높으다면 정답처리
            while stack and cur > temperature[stack[-1]]:
                last = stack.pop()
                result[last] = i - last

            stack.append(i)
            print(stack)
            print(result)


stack = Stack()
print(stack.dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73]))
