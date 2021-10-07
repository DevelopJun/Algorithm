# 카드2
from collections import deque
n = int(input())


def finalNumber(n: int) -> int:
    numberlist = [i for i in range(1, n + 1)]
    numberlist = deque(numberlist)

    while len(numberlist) > 1:
        numberlist.popleft()
        if len(numberlist) == 0:
            break
        remain = numberlist.popleft()
        numberlist.append(remain)

    return numberlist[0]


print(finalNumber(n))
