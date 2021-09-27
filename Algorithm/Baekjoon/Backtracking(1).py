# 파이썬 리스트에 있는 값들의 모든 조합을 구하기 위해서는 여러가지 방법이 있다.
# 파이썬 기본 라이브러리인 itertools 사용하면 쉽게 구할 수 있다. 하지만 각각의 차이점을
# 알고 있어야 한다.
# from itertools import combinations
# # from itertools import permutations # 콤비네이션과 동일
# from itertools import product
# items = ['1', '2', '3', '4', '5']
# a = list(combinations(items, 2))
# print(a)

from itertools import combinations  # 조합 함수
import time


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

start = time.time()

members = [i for i in range(N)]
possible_team = []

# 조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000  # 갭이 제일 작은걸 찾기 위해서
for i in range(len(possible_team)//2):
    # A 팀
    team = possible_team[i]
    stat_A = 0  # A 팀 능력치
    for j in range(N//2):
        members = team[j]  # 맴버
        for k in team:
            stat_A += S[members][k]  # 맴버와 함께할 경우의 능력치들

    # A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]  # 멤버
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))


print(min_stat_gap)
print(time.time() - start)
