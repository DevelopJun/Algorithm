def solution(record):
    answer_ready = []
    dic = {}

    for i in range(len(record)):
        # print(record[i].split(), end=' ')
        split_list = record[i].split()
        if split_list[0] == 'Enter':
            answer_ready.append(split_list[1] + " 님이 들어왔습니다.")
            dic[split_list[1]] = split_list[2]
        elif split_list[0] == 'Leave':
            answer_ready.append(split_list[1] + " 님이 나갔습니다.")
        elif split_list[0] == 'Change':
            dic[split_list[1]] = split_list[2]

    # print()
    # print('check answer ', answer_ready)
    # print('check dictionary', dic)

    answer = []
    for i in range(len(answer_ready)):
        split_list = answer_ready[i].split()
        # print(split_list)
        for l in dic:
            if split_list[0] == l:
                answer.append(dic[l] + "님이 " + split_list[2])
    # print(answer)

    return answer

# 이 코드로 할 경우에 75점의 점수 테스트 몇개가 시간초과가 발생했다.
# 시간복잡도를 On2 에서 더 낮춰야 할 것 같다.


def solution(record):
    answer_ready = []
    dic = {}

    for i in range(len(record)):
        split_list = record[i].split()
        if split_list[0] == 'Enter':
            answer_ready.append(split_list[1] + " 님이 들어왔습니다.")
            dic[split_list[1]] = split_list[2]
        elif split_list[0] == 'Leave':
            answer_ready.append(split_list[1] + " 님이 나갔습니다.")
        elif split_list[0] == 'Change':
            dic[split_list[1]] = split_list[2]

    answer = []
    # print('answer_ready', answer_ready)
    # print('dic', dic)

    for i in range(len(answer_ready)):
        split_list = answer_ready[i].split()
        # print(split_list)
        answer.append(dic[split_list[0]] + "님이 " + split_list[2])

    # print(answer)

    return answer


# 그래서 밑에 이중 반복문 줄였음.
# 시간초과 해결
ㄴ
