# 이진탐색(Binary Search) 기능을 제공하는 표준 라이브러리
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 사용

from bisect import bisect_left  # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_right
# 두 메서드 모두 시간복잡도 O(logN)


a = [1, 2, 3, 3, 3, 5, 5, 7]

print(bisect_left(a, 3))
print(bisect_right(a, 3))
print(bisect_left(a, 5))
print(bisect_right(a, 5))


a = [1, 2, 3, 3, 3, 5, 5, 7]


def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


print(count_by_range(a, 3, 3))  # 3의 개수
print(count_by_range(a, 2, 5))  # 2 이상 5 이하인 수

# https://velog.io/@janeljs/python-for-coding-test-7
