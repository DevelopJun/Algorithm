# 반복수열 # 깔끔하게 풀었다.
from collections import deque
from sys import stdin

from numpy import logical_and
read = stdin.readline

A, P = map(str, read().split())

D_list = deque()
D_list.append(A)
result = [int(A)]
#### 탐색구간 반복 수열인지 확인 ####

####
count = 1
check_number = 0
while True:
    next_number = 0
    number = str(D_list.popleft())
    for num in number:
        next_number += (int(num) ** int(P))

    if next_number in result:
        check_number += next_number
        break

    D_list.append(next_number)
    result.append(next_number)
    count += 1

final_result = []
for num in result:
    if num == check_number:
        break
    else:
        final_result.append(num)


print(len(final_result))


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
