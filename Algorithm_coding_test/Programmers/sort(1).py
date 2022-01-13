# 프로그래머스 정렬 k번째 수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        k = commands[i][2]

        sort_part1 = sorted(array[start-1:end])

        print('정렬된 리스트', sort_part1[k-1])
        answer.append(sort_part1[k-1])
    return answer
