# # 상하좌우 
# N = int(input())
# data = list(map(str, input().split()))

# x = 1
# y = 1

# for i in data:
#     if i == 'L' and y != 1:
#         y -= 1
#     if i == 'R' and y < N:
#         y += 1
#     if i == 'U' and x != 1:
#         x -= 1
#     if i == 'D' and x < N:
#         x += 1

# print(x,y)

# 4-1 답안 예시 
n = int(input())
x, y = 1, 1

plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # continue 위로 올라가라 반복문으로 

    x, y = nx, ny

print(x,y)











