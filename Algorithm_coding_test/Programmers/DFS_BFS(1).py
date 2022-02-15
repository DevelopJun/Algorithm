# 프로그래머스 타겟 넘버 (DFS, BFS) 문제

# BFS 로 풀기
from numpy import number


def solution(numbers, target):
    leaves = [0]
    answer = 0
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp

    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer


print(solution)

# DFS로 풀기
# BFS가 수평적으로 더해 한꺼번에 모든 결과값을 얻었다면, DFS 이용할때 하나씩 비교한다.


def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth + 1)
        return answer
## 결국 못 풀어서 봤음.. DFS, BFS 진짜 이해하고 싶다..

# DFS 사용 
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 # DFS 로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크 
    return answer
# 로직은 잘 생각했거든? 근데 여기서 잘 생각 못한게 뭐냐면, 1. visited 에서 반복문으로 False 돌려서 나두는거 생각 못했고, solution에서 DFS 함수
# 호출할 경우에 visitied도 같이 줘야하는걸 생각 못했다. 

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터 
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


# BFS 방법은 queue 로 그대로 뺐음. 

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)