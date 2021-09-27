# # 개미 전사 (준호 개인 코딩)

# N = int(input())
# storage = list(map(int, input().split()))

# first = []  # 첫번째로 나두고,
# second = []  # 두번째로 나두고,


# def storage1(x):
#     first.append(x)
#     return 1


# def storage2(x):
#     second.append(x)
#     return 1


# for i in range(N):
#     if i % 2 == 0:
#         storage1(storage[i])
#     else:
#         storage2(storage[i])

# print(first)
# print(second)
# print(max(sum(first), sum(second)))

# 답안 예시

n = int(input())
storage = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, n):
    # d[i-3]은 d[i-1]과 d[i-2]을 구하는 과정에서 이미 고려 되었기(계산되었기) 때문에
    d[i] = max(d[i - 1], d[i - 2] + storage[i])

print(d[n - 1])  # 이건 왜 n-1인가?
