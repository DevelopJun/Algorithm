# 순차 탐색 Sequential Search란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
# 순차 탐색 소스코드

import sys


def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오")
input_data = input().split()  # 이럴 경우에 바로 리스트 형태로 들어가구나,
print(input_data)
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))

# 이진 탐색: 반으로 쪼개면서 탐색하기
# 이진 탐색 Binary Search은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
# 찾으려는 데이터와 중간점 middle 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는게 이진 탐색 과정이다.


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 반복문으로 구현한 이진 탐색 소스코드
# 이진 탐색 소스코드 구현(반복문)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

# 이진 탐색 트리 한줄 입력 받아 출력하는 소스코드
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

print(input_data)
