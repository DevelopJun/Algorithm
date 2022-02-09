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
