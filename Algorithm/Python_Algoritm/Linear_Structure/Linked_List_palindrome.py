# 연결 리스트가 팰린드롬 구조인지 판별하라
# 입력 1 -> 2
# false
# 입력 1-> 2-> 2-> 1
# true
# 이거 입력 리스트로 받는다.
from collections import deque


def isPalindrome(nums: list[int]) -> bool:

    if not nums:
        return True

    while len(nums) > 1:
        if nums.pop(0) != nums.pop():
            return False
    return True


nums = list(map(int, input().split()))
print(isPalindrome(nums))


# 데큐로 풀려면,
def isPalindromeDeque(nums: list[int]) -> bool:
    nums = deque([nums])
    print(nums)
    if not nums:
        return True

    while len(nums) > 1:
        if nums.popleft() != nums.pop():
            return False
    return True


nums = list(map(int, input().split()))
print(isPalindromeDeque(nums))
