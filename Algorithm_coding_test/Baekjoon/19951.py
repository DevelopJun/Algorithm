# 태상이의 훈련소 생활

N, M = map(int, input().split())
H = list(map(int, input().split()))
command = []
for i in range(M):
    command.append(list(map(int, input().split())))

print(N, M)
print(H)
print(command)
print('*' * 15)
print(H[command[0][0]-1:command[0][1]])
for x in range(M):
    # k 만큼 늘어 나도록 흙을 덮어야 한다.
    if command[x][-1] >= 0:
        for l in H[command[x][0]-1:command[x][1]]:
            l += command[x][-1]

        print(H)
    else:  # k 만큼 줄어들도록 흙을 파내야 한다.
        for f in H[command[x][0]-1:command[x][1]]:
            f -= command[x][-1]
        print(H)
    print(H)
