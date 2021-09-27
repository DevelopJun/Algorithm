# 전보
import heapq
INF = int(1e9)

n, m, start = map(int, input().split())


graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
max_distance = 0

# 그니까 지금 distance에서는 start노드가 각각으로 가는 모든 이제
# 메세지를 받는 총 도시의 개수 만을 지금 알 수 있는거지, 1에서 3으로 최단 거리가 얼만지, 1에서 5로 최단거리가 얼만지 이런게 다 나와있어서


for d in distance:
    if d != INF:  # 이거 통과하면 count += 1 해줘야 하는거지
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1 을출력
print(count - 1, max_distance)
