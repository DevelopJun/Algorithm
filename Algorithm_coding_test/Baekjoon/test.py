N = int(input())
M = int(input())

graph = [list(map(int, input().split())) for _ in range(M)]

start_node = 1
visited = []
stack = [start_node]
count = []


def DFS(n, graph):
    for i in range(len(graph)):
        if graph[i][0] == n and graph[i][1] not in visited:
            stack.append(graph[i][1])
            visited.append(graph[i][1])
            count.append(1)
            DFS(stack.pop(), graph)
    return sum(count)


print(DFS(start_node, graph))
