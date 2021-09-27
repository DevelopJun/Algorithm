# 프로그램이 1

from collections import Counter


def solution(id_list, report, k):
    setting = {}

    for i in report:
        if i.split()[0] in setting and i.split()[0]:
            setting[i.split()[0]].append(i.split()[1])
            setting[i.split()[0]] = list(set(setting[i.split()[0]]))
        else:
            setting[i.split()[0]] = [i.split()[1]]

    array = list(setting.values())
    count1 = sum(array, [])

    counter = dict(Counter(count1))

    count2 = []  # k 번 이상 신고 당한 명단

    for key, value in counter.items():
        if value >= k:
            count2.append(key)

    answer = []  # 각 유저별로 처리 결과 메일을 받은 횟수

    for z in id_list:
        if z in setting:
            a = list(set(count2).intersection(setting[z]))
            answer.append(len(a))
        else:
            answer.append(0)

    return answer


# solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
#                                               "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
