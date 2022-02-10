# # DFS 와 BFS
# # DFS 는 stack 이고, BFS 는 queue 이다.

# from collections import deque
# from sys import stdin
# read = stdin.readline

# N, M, V = map(int, read().split())
# dic = {}

# DFS_result = []
# BFS_result = []

# # 딕셔너리 set 만드는 반복이지, value 값을 set 으로 만들어줘야 하는데,
# for j in range(N):
#     dic[j + 1] = set()

# for i in range(M):
#     l, n = map(int, read().split())
#     dic[l].add(n)


# stack = []
# visited_DFS = []

# print('dic이당', dic)


# def DFS(graph, V):
#     for num in dic[V]:
#         if num not in visited_DFS and num != set():
#             stack.append(num)
#             visited_DFS.append(num)
#             DFS(graph, num)
#     return(stack)


# def BFS(dic, V):
#     queue = deque([V])
#     visited_BFS = []

#     while queue:
#         n = queue.popleft()

#         if n not in visited_BFS:
#             visited_BFS.append(n)
#             # 이미 방문한 노드는 다 빼고, set 한 이유가 지금 차집합 하려는데,
#             # dic[n]이 set으로 되어 있어서, 이거 다뺴고 Queue로 다 집어 넣는 과정임,
#             # 여기서 += 이걸로 저렇게 바로 넣을 수 있는지 몰랐음.
#             queue += dic[n] - set(visited_BFS)

#     return visited_BFS


# final_DFS = DFS(dic, V)
# final_DFS.insert(0, V)
# print(final_DFS)
# print(BFS(dic, V))


#####################################################
# 결국 못풀어서 답안 참조 #


from collections import deque
import queue
from sys import stdin
read = stdin.readline

N, M, V = map(int, read().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
print(graph)

for _ in range(M):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1


def BFS(start_v):
    visited = [start_v]
    # 리스트를 써서 pop(0) 하게 되면 시간 복잡도가 O(N)이다.
    # 그래서 시간복잡도가 0(1)인 deqeue를 사용한다.

    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[start_v][w] == 1 and (w not in visited):
                visited.append(w)
                queue.append(w)


def DFS(start_v, visited=[]):
    visited.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in visited):
            # 이 visited를 계속 파라미터로 전달해줘야 하나봄..
            DFS(w, visited=[])


DFS(V)
print()
BFS(V)
