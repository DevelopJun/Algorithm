# soring 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.
# 정렬 알고리즘은 이진 탐색의 전처리 과정이기도 함.
# 오름 차순 정렬은 reverse 해서 내림차순으로 바꾸면 되는거라서 오름차순만 생각 ㄱ 어차피 연산 O(N)이라서 괜춘

# 선택 정렬 소스 코드 // 선택 정렬은 데이터를 앞으로 보내는 과정을 N - 1 번 반복하면 정렬이 완료된다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 파이썬 스와프(swap) 소스코드

array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)

# 삽입 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# 퀵 정렬
# 퀵 정렬에서는 피벗이 사용된다. 기준을 바로 피벗이라고 한다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 퀵 정렬 (이거 보는게 훨 쉬움)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번쨰 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    # 하 드디어 이해했다. 그니까 왼쪽으로 들어간 새끼들 return으로 왼쪽만 죽어라 파다가 다 되면 [pivot] 이랑 결합되고,
    # 그 뒤에 right side 오른쪽으로 들어간 새끼들 return으로 오른쪽만 죽어라 파다가 결국 모두 return 으로 리스트
    # 형태로 나오게 되는거임.


print(quick_sort(array))

# 계수 정렬
# 계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
# 근데 계수 정렬은 별도의 리스트를 선언하고 그 안에 정렬을 담는거라서, 비교하는게 아니라 그 데이터 크기가 매우 중요함.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end='')  # 띄어 쓰기 구분하려고
