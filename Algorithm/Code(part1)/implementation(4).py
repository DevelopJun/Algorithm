# 게임개발 실전문제 답안 예시

N, M = map(int, input().split())

d = [[0]*M for _ in range(N)]
# 컴프리핸션 문제 까먹으면 안된다. 2차원 리스트 선언할때는 컴프리 헨션을 사용하는게 훨씬 효과적임.

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서, 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는거 지금 시계 반대방향인데, 서쪽이 3, 남쪽이 2 동쪽이 1 북쪽이 0인데 여기서 북쪽에서 서쪽으로 다시 돌아가기
# 위해서 if direction == -1: direction = 3 을 쓴거임
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]


    if d[nx][ny] == 0 and array[nx][ny] == 0: # 지금 원래 d에서 위치 0으로 만들고 본인이 있던곳 1로 설정했으니, 0인곳은 안가본 곳이고, array는 육지랑 바다 체크하는거임.
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue # 여기서 continue 했을때 어디로 가는가? 
    else:
        turn_time += 1

    # 4방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    
print(count)
