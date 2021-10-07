'''
자료구조는 크게 메모리 공간 기반의 연속 Contiguous 방식과 포인터 기반의 연결 Link 방식으로 나뉜다.
배열은 이 중에서 연속 방식의 가장 기본이 되는 자료형이다.

대부분의 언어에서 동적 배열을 지원하며, 자바에서는 ArrayList, C++ std:vector가 대표적인 동적 배열 자료형이다.

파이썬에는 정적 배열 자체가 없다. 동적 배열 리스트만 제공한다.
'''

# 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

# 브루트 포스로 푸는 방법 -> 시간 복잡도 O(n2)
nums = [2, 7, 11, 15]
target = 9


def targetcollect1(target: int) -> list[int]:
    for i in range(len(nums)):
        for x in range(len(nums)-1):
            if(nums[i] + nums[x+1] == target):
                return [i, x + 1]


print(targetcollect1(target))

# in 과 enumerate로 푸는 방법 -> 시간 복잡도 O(n2) -> 같은 시간 복잡도라도 in 연산쪽이 훨씬 더 가볍고 빠르다.


def targetcollect2(target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


print(targetcollect2(target))

# 첫 번째 수를 뺀 결과 키 조회 -> 전체 시간복잡도 O(n), 딕셔너리는 해시 테이블로 구현되어 있고, 이 경우 조회는 평균적으로 O(1)에 가능하다.


def targetcollect3(target: int) -> list[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    print(nums_map)
    # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


print(targetcollect3(target))

# 투 포인터 이용
'''
투 포인터란 왼쪽 포인터와 오른쪽 포인터의 합이 타켓보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서
값을 조정하는 방식이다. 

근데 여기서 문제가 존재하는데, 만약에 target 이 정렬 되어 있지 않으면, sort 로 
정렬을 해야한다. 근데, 여기서 sort로 정렬을 했을때, index값이 뒤죽박죽이 되기 때문에 two point로 이것을 풀 수가 없다. 

'''


def twoSum(target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타켓보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


print(twoSum(target))
