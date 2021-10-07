# 미로 찾기 준호 개인 코딩
from collections import deque
N, M = map(int, input().split())

count = 1

total = []

for i in range(N):
    total.append(list(map(int, input())))


def bfs(x, y):
    global count
    if x == M and y == N:
        print(count)
    else:
        if total[x-1][y] != 0 and y + 1 <= M:
            y += 1
            count += 1
            bfs(x, y)
        if total[x][y-1] != 0 and x + 1 <= N:
            x += 1
            count += 1
            bfs(x, y)


bfs(1, 1)

# 예시 답안


n, m = map(int, input().split())

total = []
for i in range(n):
    total.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지  반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if total[nx][ny] == 0:
                continue
            # 괴물 없는 구간,
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if total[nx][ny] == 1:
                total[nx][ny] = total[x][y] + 1  # 이걸 2, 3 계속 데리고 가는거네 ㅁㅊ
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return total[n-1][m-1]


print(bfs(0, 0))
