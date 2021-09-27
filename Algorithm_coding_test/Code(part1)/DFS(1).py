# 음료수 얼려먹기 ㄴㄴ준호 개인 코드
N, M = map(int, input().split())

count = 0

ice = []
for i in range(N):
    ice.append(list(map(int, input())))


def dfs(ice, x, y, visited):
    global count
    visited[x][y] = 'True'

    if x > 0:
        if ice[x-1][y] == 0 and visited[x-1][y] == 'False':
            dfs(ice, x-1, y, visited)
    if ice[x+1][y] == 0 and visited[x+1][y] == 'False':
        dfs(ice, x+1, y, visited)
    if y > 0:
        if ice[x][y-1] == 0 and visited[x][y-1] == 'False':
            dfs(ice, x, y-1, visited)
    if ice[x][y+1] == 0 and visited[x][y+1] == 'False':
        dfs(ice, x, y+1, visited)
    count += 1

    index_l = 0
    index_z = 0
    for l in visited:
        index_l += 1
        for z in l:
            index_z += 1
            if z == 'False':
                dfs(ice, index_l, index_z, visited)

    return False


visited_basis = ['False'] * M  # 행 14개 들어간다.

visited = []  # 열 만들려고
for i in range(N):
    visited.append(visited_basis)
print(visited)

dfs(ice, 0, 0, visited)


print(count)

# 음료수 얼려먹기 답안예시
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기

ice = []
for i in range(n):
    ice.append(list(map(int, input())))


def dfs(x, y):
    if x <= 1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        # 해당 노드 방문 처리
        ice[x][y] == 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
