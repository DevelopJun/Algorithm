# 시간초과 문제 발생
# import sys

# from numpy import zeros
# N = int(sys.stdin.readline())


# def fibonacci(n):
#     zero = []
#     one = []
#     if n == 0:
#         zero.append(0)
#         return 0
#     elif n == 1:
#         one.append(1)
#         return 0
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# for i in range(N):
#     n = int(sys.stdin.readline())
#     fibonacci(n)

# 다시 문제 풀기 시작함.

t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = zero + one
        zero = tmp
    print(zero, one)
