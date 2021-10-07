

def solution(info, edges):
    visited = [False] * len(info)
    print(visited)

    #########################################

    def dfs(edges, v, visited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v, end=' ')
        print(edges)
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in edges[v]:
            if not visited[i]:
                dfs(edges, i, visited)

    dfs(edges, 0, visited)

    ##########################################

    answer = 0
    return answer


solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
         0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
