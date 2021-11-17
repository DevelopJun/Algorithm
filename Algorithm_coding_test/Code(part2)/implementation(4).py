# 외벽점검  / 프로그래머스에서 직접 풀어야함.
import copy
from itertools import combinations as combi


def solution(n, week, dist):
    dst = copy.deepcopy(dist)
    dst.sort(reverse=True)

# 제일 많은 거리를 갈 수 있는 사람을 어디에 배치하는지 먼저 계산한 이후에,
# 나머지를 구현해야 하는가?
    for i in range(1, len(dst) + 1):
        # week = [1, 5, 6, 10]
        for item in combi(range(len(week)), i):
            # 0, 1
            d = []
            for j in range(i):
                # 여기 부분이 이해가 안됩니다.
                d.append((week[item[(j+1) % i]-1]-week[item[j]] + n) % n)
            d.sort(reverse=True)
            rst = True
            for j in range(i):
                if dst[j] < d[j]:
                    rst = False
                    break
            if rst:
                return i
    answer = -1

# 시계 방향으로 떨어진 거리


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))


# 이해가 안되는데,
