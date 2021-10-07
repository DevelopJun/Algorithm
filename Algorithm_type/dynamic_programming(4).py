# 효율적인 화폐 구성
n, m = map(int, input().split())

money = []

for _ in range(n):
    number = int(input())
    money.append(number)
    # money.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
# 근데 이거 뭔가 변경된거지
money = [2, 3]

for i in range(n):  # K 선택 money[i] -> K
    for j in range(money[i], m + 1):  # 인덱스
        # (i - k)원을 만드는 방법이 존재하는 경우 왜 i - K 를 하느냐?
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j-money[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
