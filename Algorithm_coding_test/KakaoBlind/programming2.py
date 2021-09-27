import string

tmp = string.digits+string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


print(convert(437674, 3))

# 소수 판별 알고리즘


def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # i로 나누어 떨어지면 소수가 아니므로 False 리턴

    return True  # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴


def solution(n, k):
    converse = convert(n, k)  # 진수 변환
    converselist = list(map(int, str(converse)))
    print(converselist)

    answer = -1
    return answer


solution(437674, 3)
