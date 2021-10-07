from collections import deque
import collections


def ExceptSelf(nums: list[int]) -> list[int]:
    result = []
    deq = collections.deque(nums)
    print(deq)

    for i, n in enumerate(nums):
        deq.remove(n)
        result.append(list(deq))

        deq.appendleft(n)
        print(deq)

    print(result)

    sum = 1
    finalresult = []
    for z in range(len(nums)):
        result[z]
        pass

    return 0


ExceptSelf([1, 2, 3, 4])


def productExceptSelf(nums: list[int]) -> list[int]:
    # out = []
    # p = 1
    # # 왼쪽 곱셉
    # for i in range(0, len(nums)):
    #     out.append(p)
    #     p = p * nums[i]
    # p = 1
    # # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    # for i in range(len(nums) - 1, 0 - 1, -1):
    #     out[i] = out[i] * p
    #     p = p * nums[i]

    # print(out)

    # return 0

    # print(productExceptSelf([1, 2, 3, 4]))
