
from typing import List
s = ["h", "e", "l", "l", "o"]

# 1. 일반적인 방식


class Solution1:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# 2. 파이썬 다운 방식


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
