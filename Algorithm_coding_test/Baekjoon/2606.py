# # 바이러스 문제 # DFS 스택이고, # BFS 는 Queue 이다.


# N = int(input())
# M = int(input())

# graph = [list(map(int, input().split())) for _ in range(M)]

# start_node = 1
# visited = []
# stack = [start_node]

# # def solution(start_node, graph):
# #     start_node = DFS(start_node, graph)
# #     return answer

# count = []


# def DFS(n, graph):
#     print('그래프 모양', graph)
#     print('n', n)

#     for i in range(len(graph)):
#         if graph[i][0] == n and graph[i][1] not in visited:
#             stack.append(graph[i][1])
#             print('Stack 입니다.', stack)
#             visited.append(graph[i][1])
#             print('visited 입니다.', visited)
#             count.append(1)
#             DFS(stack.pop(), graph)
#             print('DFS 실행 되었습니다.')

#     return sum(count)


# # print(solution(start_node, graph))
# print(DFS(start_node, graph))


# 문제 못 풀어서 다시 DFS 방식 다른 사람들이 푼거 참조했음.

from sys import stdin
read = stdin.readline  # 와 이걸 input으로 뿌숨.

dic = {}

for i in range(int(read())):
    dic[i+1] = set()

print(dic)

# 딕셔너리 만드는 구조
for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

# dfs 함수 구조

print(dic)


def DFS(start, dic):
    for i in dic[start]:
        print(i)
        if i not in visited:
            visited.append(i)
            DFS(i, dic)


visited = []
DFS(1, dic)

print(visited)
print(len(visited)-1)
