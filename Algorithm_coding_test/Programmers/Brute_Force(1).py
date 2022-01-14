# 완전탐색은 브루트 포스 임.
def solution(answers):
    # 앞에서 반복문으로 넘겨주기
    first_person = [1, 2, 3, 4, 5]
    second_person = [2, 1, 2, 3, 2, 4, 2, 5]
    third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # answers = [1, 2, 3, 4, 5]
    # answers = [1, 3, 2, 4, 2]
    first = 0
    second = 0
    third = 0

    answer = []
    for i in range(len(answers)):
        if answers[i] == first_person[i]:
            first += 1
        if answers[i] == second_person[i]:
            second += 1
        if answers[i] == third_person[i]:
            third += 1

    pre_check = []
    pre_check.append(first)
    pre_check.append(second)
    pre_check.append(third)

    # print(max(pre_check))
    max_number = max(pre_check)

    check = [(v, i) for i, v in enumerate(pre_check)]
    # print(check)

    answer = []
    for i in range(len(check)):
        if check[i][0] >= max_number:
            answer.append((check[i][1] + 1))

    return answer
##


def solution(answers):
    first_person = [1, 2, 3, 4, 5] * 10000
    second_person = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    print(first_person)
    first = 0
    second = 0
    third = 0

    answer = []
    for i in range(len(answers)):
        if answers[i] == first_person[i]:
            first += 1
        if answers[i] == second_person[i]:
            second += 1
        if answers[i] == third_person[i]:
            third += 1

    pre_check = []
    pre_check.append(first)
    pre_check.append(second)
    pre_check.append(third)

    max_number = max(pre_check)

    check = [(v, i) for i, v in enumerate(pre_check)]

    answer = []
    for i in range(len(check)):
        if check[i][0] >= max_number:
            answer.append((check[i][1] + 1))

    return answer
