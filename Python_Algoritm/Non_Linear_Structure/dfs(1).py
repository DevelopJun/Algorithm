# 섬의 개수 문제
# 입력값 :
# 11110
# 11010
# 11000
# 00000

def numIslands(grid: list[list[str]]) -> int:
    def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종류
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 0

        # 동서남북탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 이후에 카운트 1 증가
                count += 1
    return count


grid = []
for _ in range(5):
    number = list(map(str, input()))
    grid.append(number)

print(grid)
print(numIslands(grid))
