'''
체스판 다시 칠하기
'''
from abc import abstractproperty


N, M = map(int, input().split())
orginial = []
count = []

for _ in range(N):
    orginial.append(input())

for a in range(N-7):
    for b in range(M-7):
        case1 = 0
        case2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 이게, 특정하게 체스 판 같은 경우에 2로 나눴을때 0이 나오는 짝수인지, 홀수인지 규칙이 존재하기 때문임.
                # 이 부분은 계속 짝수 부분을 잡는것
                if (i+j) % 2 == 0:
                    if orginial[i][j] != "W":
                        case1 += 1
                    if orginial[i][j] != "B":
                        case2 += 1

                # 이 부분은 계쏙 홀수 부분을 잡는 것
                else:
                    if orginial[i][j] != "B":
                        case1 += 1
                    if orginial[i][j] != "W":
                        case2 += 1

        count.append(min(case1, case2))

print(min(count))
