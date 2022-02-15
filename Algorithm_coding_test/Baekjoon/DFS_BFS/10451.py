# 순열 사이클 ########## 드디어 DFS 풀었어!! 점점 이해하고 있음 !!!
from sys import stdin
read = stdin.readline

test_case = []
T = int(read())  # 입력 케이스

final_result = []

for i in range(T):
    # 각 그래프 딕셔너리 구상
    dic = {}
    N = int(read())  # 순열의 크기
    test_number = list(map(int, read().split()))
    for l in range(1, N + 1):
        dic[l] = test_number[l - 1]
    test_case.append(dic)

    ### DFS 시작 구간 ###
    answer = 0
    visited = [False for i in range(N + 1)]

    def DFS(dic, num, visited):
        if visited[num] == False:
            visited[num] = True
            DFS(dic, dic[num], visited)

    for num in range(1, N + 1):
        if visited[num] == False:
            DFS(dic, num, visited)
            answer += 1

    final_result.append(answer)

for num in final_result:
    print(num)
