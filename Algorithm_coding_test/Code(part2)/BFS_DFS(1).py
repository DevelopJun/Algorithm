# 특정 거리의 도시 찾기

# N: 도시의 개수, M: 도로의 개수, K: 거리의 정보, X: 출발 도시의 번호

# 입력 부분
from typing import Deque


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # 딕셔너리 어려우니까 이런식으로 리스트에서 인덱스 잡고 가는 곳 정의했네,

# 모든 도로 정보 입력 받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

print(graph)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = Deque([X])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

# 만약 최단 거리가 K인 도서가 없다면, - 1 출력
if check == False:
    print(-1)
