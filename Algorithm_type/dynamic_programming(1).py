# 1로 만들기 준호 개인 코딩

count = 0


def fibo(x):
    global count
    count += 1
    if x == 1:
        return 1
    else:  # 우선순위를 찾지 못하겠음. ㅅㅂ
        fibo(x - 1)
        if x % 5 == 0:
            fibo(x // 5)
        elif x % 3 == 0:
            fibo(x // 3)
        elif x % 2 == 0:
            fibo(x // 2)
        else:
            fibo(x - 1)


fibo(int(input()))

print(count)

# 답안 예시
# 정수 X 를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
