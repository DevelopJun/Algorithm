# 완주하지 못한 마라톤 선수
import collections
from typing import Counter


def solution(participant, completion):
    extract = []
    duplicate = Counter(participant)

    for i in range(len(participant)):
        if participant[i] not in completion:
            extract.append(participant[i])

    if len(extract) == 0:
        for key, value in duplicate.items():
            if value > 1:
                extract.append(key)

    answer = "".join(extract)
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

### 위에 시간 초과 ####


def solution(participant, completion):
    pass_list = []  # 완주한 인간들
    return_list = []  # 완주 못한 인간들
    extract = []  # 중복된 인간들

    for i in range(len(participant)):
        if participant[i] not in completion and participant[i] not in pass_list:
            return_list.append(participant[i])  # 완주 못한 인간들
        elif participant[i] in completion and participant[i] not in pass_list:
            pass_list.append(participant[i])  # 완주한 인간들
        elif participant[i] in pass_list and participant[i] in pass_list:
            extract.append(participant[i])  # 중복된 인간들

    print('완주한 인간들', pass_list)
    print('완주 못한 인간들', return_list)
    print('중복된 인간들', extract)

    if len(return_list) == 0:
        answer = "".join(extract)
    else:
        answer = "".join(return_list)

    return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# 시간초과 2번 맞고, O(n2) 프로그래머스 풀이 봤음. 이거 우쩨 이렇게 풀었노,;;;


def solution(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# counter는 participant의 각 요소들과 그 개수를 짝지어서 가지고 있기 때문에, 겹치는 요소들의 개수를 빼서 결과적으로
# answer에는 단 하나의 이름(key)과 1(value)만 남게 된다. 따라서 answer.keys()를 list로 만들어주면
# 0 번째 인덱스가 완주하지 못한 선수의 이름이다
