# # 1 이 될 때까지
# N, K = map(int, input().split())
# count = 0

# while N != 1:
#     if N % K == 0:
#         N = N//K
#     else:
#         N -= 1
#     count += 1

# print(count)

# # 3-5 답안 예시 
# N, K = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= K
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1
# print(result)

# 3-6 
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k # 
    result += (n - target) # result 나머지가 된다
    n = target # 더이상 나머지가 생기지 않고 나눌려고
    if n < k:
        break
    n //= k 
    result += 1

result += (n-1)
print(result)
