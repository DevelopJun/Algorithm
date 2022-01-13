# 프로그래머스 동적 계획법 N으로 표현 문제
def solution(N, number):
    dp_table = [[]]
    for i in range(1, 9):  # N 조건이자 사용 횟수 조건
        case = []
        for j in range(1, i):
            for k in dp_table[j]:
                for l in dp_table[i - j]:
                    case.append(k + l)  # 더하기
                    if k - l >= 0:
                        case.append(k - l)  # 빼기
                    case.append(k * l)  # 곱하기
                    if l != 0 and k != 0:
                        case.append(k // l)  # 나누기

        case.append(int(str(N) * i))  # 숫자를 그대로 이어 붙인 케이스

        if number in case:
            return i

        dp_table.append(list(set(case)))

    return -1


print(solution(5, 12))
# print(solution(2, 11))
