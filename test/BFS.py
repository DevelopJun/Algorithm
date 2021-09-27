# BFS breath first search 알고리즘은 너비 우선 탐색이라는 의미를 가진다. 가까운 노드부터 탐색하는 알고리즘임.
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는데, BFS 는 그 반대임. 
# 큐 자료구조 사용
# deque 라이브러리를 사용하는 것이 좋으며, 탐색을 수행함에 있어서 O(N)의 시간이 소요된다. 
# DFS보다는 BFS가 좀 더 빠르게 움직인다는 것을 기억하자

from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)