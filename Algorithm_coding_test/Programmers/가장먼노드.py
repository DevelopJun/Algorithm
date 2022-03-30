import heapq


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    print(graph)
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    for i in graph:
        print(i)

    inf = int(1e9)
    distance = [inf] * (n+1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))  # (거리, 노드)

    def go(start):  # start => 1
        while q:
            dist, now = heapq.heappop(q)

            if dist > distance[now]:  # dist가 거리,
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    go(1)
    print(distance)
    answer = 0

    return answer
