# n 개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# [1, 4, 3, 2]
import sys


def arrayPairSum(nums: list([int])) -> int:
    sum = 0
    pair = []
    nums.sort()
    print(nums)

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 게산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# print(arrayPairSum(list(map(int, sys.stdin.readline().split()))))

def arrayPairSum1(nums: list([int])) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):

        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum


# print(arrayPairSum1(list(map(int, sys.stdin.readline().split()))))

# 이렇게 한줄로 코딩할 수도 있다.
def arrayPairSum1(nums: list([int])) -> int:
    return sorted(nums)[::2]
