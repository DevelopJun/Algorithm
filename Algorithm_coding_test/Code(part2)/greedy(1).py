# 모험가 길드 
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 1 2 2 2 3
result = 0 
count = 0


for i in range(N):
    val = arr[i] # var 라는 숫자가 여태 count 올린 수와 같다는 것은 그 앞을 포함 할 수 있다는 말
    count += 1
    if val == count:
        result += 1
        count = 0

print(result)

