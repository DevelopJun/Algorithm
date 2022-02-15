# 멀쩡한 사각형 summer/winter coding(2019)
# 이해가 안된다 진심으로

import math


def solution(w, h):
    return w*h - (w + h - math.gcd(w, h))


print(solution(9, 6))

# 서로소 , 최대공약수 확인
