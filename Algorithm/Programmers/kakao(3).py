# # orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# # orders = ["XYZ", "XWY", "WXA"]
# # course = [2, 3, 4]
# course = [2, 3, 5]
# course = [2, 3, 4]

# array = []

# for i in range(len(orders)):
#     for z in range(i+1, len(orders)):
#         overlap = list(set(orders[i]).intersection(orders[z]))
#         string2 = sorted(overlap)
#         string3 = "".join(string2)
#         array.append(string3)

# print(array)
# lost = []

# for i in range(len(course)):
#     for z in range(len(array)):
#         if(len(array[z]) == course[i] and ):
#             lost.append(array[z])

# print("course 통과 ", lost)

# lost2 = list(set(lost))
# lost2.sort()
# print(lost2)

###################################

# # 2번째 예제에서 왜 "AB" 가 포함되지 않고 있는지 이해를 하지 못하고 있음.
# # https://programmers.co.kr/learn/courses/30/lessons/72411

#######################################

from collections import Counter
from itertools import combinations, count


def solution(orders, course):
    answer = []
    for c in course:
        temp = []

        for order in orders:
            combi = list(combinations(sorted(order), c))
            temp += combi
        # 끝난거임 for은

        counter = Counter(temp)
        print('*' * 10)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            for f in counter:
                if(counter[f] == max(counter.values())):
                    answer += [''.join(f)]
            # answer += [''.join(f) for f in counter if counter[f]
            #            == max(counter.values())]

    return sorted(answer)


print(solution(orders, course))
