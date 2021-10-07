# DFS은 Depth-first search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
# 노드, 간선 개념의미, 그래프 탐색은 노드들을 방문하는 것을 의미


# 인접행렬(adjacency matrix) : 2차원 배열로 그래프의 연결관계를 표현하는 방식
INF = 999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0],
]

print(graph)

# 인접 리스트(adjacency list) : 리스트로 그래프의 연결 관계를 표현하는 방식

# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for in range(3)]
# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)

# DFS
# DFS 메서드 정의


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # visited[i] == False:  # 여기서 not visited[i]라고 하면 True, False boolean 타입을 말하는건가?
        if not visited[i]:
            dfs(graph, i, visited)


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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
