# 부품 찾기 준호 개인 알고리즘

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
target = list(map(int, input().split()))
target.sort()

for i in range(M):
    result = binary_search(array, target[i], 0, n-1)
    if result == False:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 답안 예시(계수 정렬)
# N(가게의 부품 개수)을 입력 받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1
# M(손님이 확인 요청한 부품 개수)을 입력 받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
