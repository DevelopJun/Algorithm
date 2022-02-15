# 기능 개발
from collections import deque


def solution(progresses, speeds):
    listed = [(progresses[i], speeds[i]) for i in range(len(progresses))]
    time = []
    for num in listed:
        count = num[0]
        check = 0
        while count < 100:
            count += num[1]
            check += 1
        time.append(check)

    # print(time)
    answer = []

    time = deque(time)

    first = time[0]
    # print(first)
    count = 1
    for i in range(1, len(time)):
        # print('count 변화', count)
        if first >= time[i]:
            count += 1
            if i+1 == len(time):
                answer.append(count)
                break
        else:
            answer.append(count)  # count 가 값이 들어가는 구간
            first = time[i]
            count = 1
            if first == time[len(time) - 1]:
                answer.append(count)
                break

    #     print(answer)
    #     print(first)
    # print('정닶', answer)

    return answer
# 어렵게 겨우 그래도 끝까지 푼 문제
