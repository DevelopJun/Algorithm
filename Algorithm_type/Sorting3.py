# 두 배열의 원소 교체
# 준호 개인 코딩
N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B = sorted(B, reverse=True)

result = []

for i in range(K):
    if A[i] < B[i]:
        result.append(B[i])

print(result)  # result 확인할려고 넣은겅미

result = result + A[K:]

print(sum(result))

# 예시 답안
N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B = sorted(B, reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
