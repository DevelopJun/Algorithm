# DFS -> 스택
# BFS -> 큐

def solution(n, computers):
    dic = {}
    for l in range(n):
        dic[l + 1] = []

    for i in range(n):
        for l in range(n):
            if i != l and computers[i][l] == 1 and dic[i + 1] == []:
                dic[i + 1] = [l + 1]
            elif i != l and computers[i][l] == 1:
                dic[i + 1].append(l+1)

    print(dic)
    print(dic[1])
    answer = 0
    visited = []
    # 그래프에서 BFS, DFS 만들기

    def DFS(dic, target):
        for num in dic[target]:
            if num not in visited:
                visited.append(num)  # 방문한 곳 기록
                DFS(dic, num)  # 여기서 지금 키를 DFS에 넣어야 하는데 value를 넣었구나

    DFS(dic, 2)
    while len(visited) < n:
        DFS(dic, 1)
        print('방문 노드 확인', visited)
        answer += 1

    return answer
