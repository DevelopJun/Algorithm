# coding test pratice / stack & queue

from collections import deque
from typing import Deque


def solution(priorities, location):
    my_print = priorities[location]  # 잡은 숫자

    deq = Deque([(v, i) for i, v in enumerate(priorities)])

    answer = 0

    while True:

        extract = deq.popleft()
        if deq and max(deq)[0] > extract[0]:
            deq.append(extract)
        else:
            answer += 1
            if extract[1] == location:
                break
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
