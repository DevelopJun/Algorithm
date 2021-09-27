from itertools import permutations
from itertools import combinations
import time

a, b = map(int, input().split())
arr = list(map(int, input().split()))
start = time.time()


# arr1 = list(permutations(arr, 2))
items = list(combinations(arr, 2))
# print(arr1)
i = 0
for item in items:
    if(item[0] == item[1]):
        del items[i]
    i += 1

print(len(items))

print(time.time() - start)

# 위에는 현재 조합 함수를 이용했고, 
# 모범 답안에서는 조합함수 사용안했음. 
# 뭔말임 동빈아

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# array = [0] * 11

# for x in data:
#     array[x] += 1

# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리 
# print(array)

# for i in range(1, m + 1):
#     n -= array[i] # 무게가 i 인 볼리공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기 
#     print("n :", n)
#     print(array[i])
#     print(result)
#     print("*" * 10)

# print(result)
