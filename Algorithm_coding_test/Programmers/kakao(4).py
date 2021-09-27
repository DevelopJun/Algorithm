# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
# 시간초과 걸렸음.


import bisect
from itertools import combinations


def solution(info, query):
    infoa = []
    for i in range(len(info)):
        infoc = info[i].split()
        infoa.append(infoc)

    querya = []
    for z in range(len(query)):
        q = query[z].replace("and", "")
        queryc = q.split()
        querya.append(queryc)

    answer = [[0] * len(querya)]

    for w in range(len(querya)):
        for l in range(len(infoa)):
            num = 0
            for s in range(5):
                if(num == 4 and s == 4 and int(querya[w][s]) <= int(infoa[l][s])):
                    num += 1
                elif(querya[w][s] == infoa[l][s] or querya[w][s] == '-'):
                    num += 1

                if(num == 5):
                    answer[0][w] += 1

    return answer[0]

######################
# 시간초과 발생해서 다른 사람 코드 보고 풀어봄,


def solution(info, query):
    answer = []
    info_dict = {}
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        print(conditions)
        print(score)
        for j in range(5):
            for c in combinations(conditions, j):
                key = ''.join(c)
                if info_dict.get(key) is None:
                    info_dict[key] = [score]
                else:
                    info_dict[key].append(score)
    print("***" * 10)
    print(info_dict)
    # 모르겠어..
    # https://www.youtube.com/watch?v=izxzh0rQxSI
    # 유튜브 참조하자. 내일 모듈 정리 싹다 하자... 정신 안차리지?

    # for key in info_dict.keys():
    #     info_dict[key] = sorted(info)


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],

               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]
               ))
