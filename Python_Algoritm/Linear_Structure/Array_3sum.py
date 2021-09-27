# 배열의 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
# nums = [-1, 0, 1, 2, -1, -4]

# 이렇게 풀어도 괜찮은데,
from itertools import combinations

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
select = list(combinations(nums, 3))
result = []

for i in select:
    if sum(i) == 0 and list(i) not in result:
        result.append(list(i))

print(result)


# 브루트 포스로 풀기
def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])


threeSum(nums)

# 투 포인트 이해 X
