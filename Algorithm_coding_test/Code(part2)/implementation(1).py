# 기둥과 보 설치
Plillar = [[]]
Bar = [[]]


def checkPillar(x, y):
    # y 가 0 이거나 (당연히 바닥은 다 가능하니까), 기둥을 설치하는 밑에 기둥이 있으면
    if y == 0 or Plillar[x][y-1]:
        return True
    # 보 위에 있는 경우도 생각해야지, 보 위에는 기둥 설치 가능하니까 .
    # 여기서 0 보다 크다고 주는 이유는 x 가 0일떄 범위를 벗어날 수 도 있어서.
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]:
        return True
    return False


def CheckBar(x, y):
    # 바로 밑에 기둥 있거나, 끝나는 지점에서(오른쪽) 밑에 기둥 있거나
    if Plillar[x][y-1] or Plillar[x+1][y-1]:
        return True
    if (x > 0 and Bar[x-1][y]) and Bar[x+1][y]:  # 왼쪽 오른쪽에 보가 있으면 가능하다.
        return True
    return False


def canDelete(x, y):  # 삭제할 수 있는 판별한다.
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            # 삭제한 것 때문에 False 가 나온건데,
            if Plillar[i][j] and checkPillar(i, j) == False:
                return False
            if Bar[i][j] and CheckBar(i, j) == False:
                return False
        return True


def solution(n, build_frame):
    global Plillar, Bar
    # 여기서 Range 범위를 +2 로 한 이유는 checkBar 함수 실행시에, x+1 이 list out of index 발생시키지 않을려고,
    Plillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for x, y, kind, cmd in build_frame:
        if kind == 0:  # 0 인거는 기둥
            if cmd == 1:  # cmd 설치 여부
                if checkPillar(x, y):  # 기둥 설치 가능한지 함수 정의
                    Plillar[x][y] = 1
            else:
                Plillar[x][y] = 0
                if not canDelete(x, y):  # false 면
                    Plillar[x][y] = 1  # 다시 복원 하는거지,
        else:  # 1 인거는 보라는 말임.
            if cmd == 1:  # cmd는 설치여부
                if CheckBar(x, y):  # 보 설치 가능한지 함수 정의
                    Bar[x][y] = 1
            else:
                Bar[x][y] = 0
                if not canDelete(x, y):
                    Bar[x][y] = 1

    answer = []
    for x in range(n+1):  # x 좌표 먼저라고 해서 먼저 넣어주고,
        for y in range(n+1):
            if Plillar[x][y]:  # 기둥이 보보다 먼저 오라고 해서, append 먼저 넣어주고,
                answer.append([x, y, 0])
            if Bar[x][y]:
                answer.append([x, y, 1])

    return answer
