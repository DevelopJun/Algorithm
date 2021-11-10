# 치킨배달 삼성전자 SW 역량 테스트 / 직접  풀었음.
from itertools import combinations  # 조합함수 사용 위해서 combinations 들고옴.

N, M = map(int, input().split())

map = list(list(map(int, input().split())) for _ in range(N))  # 지도 입력

house_location = []  # 집 위치
chicken_location = []  # 치킨 집 위치


# 집과 치킨집 좌표 추출
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:  # 집 확인
            x = i + 1
            y = j + 1
            house = [x, y]
            house_location.append(house)

        if map[i][j] == 2:  # 치킨집 확인
            x = i + 1
            y = j + 1
            chicken = [x, y]
            chicken_location.append(chicken)

if len(chicken_location) <= M:  # 치킨집이 줄여야 되는 요구사항 값보다 작거나 같으면 그대로 모두 폐업하지 않는다.
    # print(house_location)
    # print(chicken_location)
    distance = []
    for i in range(len(house_location)):
        dis = []
        for j in range(len(chicken_location)):
            distance_c = abs(house_location[i][0] - chicken_location[j][0]) + abs(
                house_location[i][1] - chicken_location[j][1])
            dis.append(distance_c)

        result = min(dis)  # 치킨집과의 거리를 하나씩 모두 계산해서, 그것 중에 제일 작은 값을 추출

        distance.append(result)  # 치킨집과의 거리 최종 최솟값 리스트 넣기
    # print(distance)

else:
    # print(house_location)
    # print(chicken_location)
    # # 치킨집 최대 M 개를 골랐을때, 경우의 수 조합함수 사용
    result = list(combinations(chicken_location, M))
    # print(result)
    return_value = []
    for i in range(len(result)):
        chicken_location = result[i]  # 조합함수로 뽑은 각 경우의 수 하나씩 치킨집으로 가정해서 반복

        distance = []

        for j in range(len(house_location)):
            dis = []
            for l in range(len(chicken_location)):
                distance_c = abs(house_location[j][0] - chicken_location[l][0]) + abs(
                    house_location[j][1] - chicken_location[l][1])
                dis.append(distance_c)

            result1 = min(dis)

            distance.append(result1)

        # 각 조건당 각 거리들 return value 최종 리스트 삽입
        return_value.append(sum(distance))

    return_value2 = min(return_value)  # 최종 리스트에서 가장 작은 값 추출 / 값 반환
