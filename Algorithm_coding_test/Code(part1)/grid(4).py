# 숫자 카드 게임 준호 개인 풀이
N, M = map(int, input().split())

total = []

for i in range(N):
    total_basis = list(map(int, input().split()))
    total_basis.sort()
    total.append(total_basis)

result = []

for i in total:
    result.append(i[0])

result.sort()
print(result[-1])

# min()함수 이용하는 답안 예시
# o(N)
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# N, M 을 공백으로 구분하여 입력받기
# O(N2)
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
