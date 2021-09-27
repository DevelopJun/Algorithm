# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.
# 입력 [7, 1, 5, 3, ,6 ,4]

# 브루트 포스 -> 시간 복잡도 O(n2)
import sys


def maxProfit(nums: list[int]) -> int:
    result = 0

    # 하나씩 돌려가면서 비교해서 제일 많이 먹은거 가지고 오는거지
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            compare = -(nums[i] - nums[j])
            result = max(result, compare)

    print(result)
    return result


maxProfit([7, 1, 5, 3, 6, 4])


# 시간 복잡도 O(n)
def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize  # 파이썬에서는 숫자형은 임의 정밀도를 지원하며 사실상 무한대의 값을 지정할 수있다.
    # 아무리 큰 수라 할지디라도 얼마든지 더 큰수가 지정될 수 있으므로, 999999 이런식으로 최솟값 변수에 임의의 값을 초기값으로
    # 지정하는 것은 지양해야 한다.
    print(min_price)
    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


maxProfit([7, 1, 5, 3, 6, 4])
