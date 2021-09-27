# 떡볶이 떡 만들기 준호 개인 코딩
M, N = map(int, input().split())
total = list(map(int, input().split()))

H = 1

while True:
    middle = []  # 확인 해보는 중간 리스트
    for i in total:
        remain = i - H
        if remain >= 0:
            middle.append(remain)
        else:
            middle.append(0)
    if int(sum(middle)) == N:
        break
    else:
        H += 1

print(H)

# 전형적인 파라메트릭 서치(Parametric Search) 유형의 문제임. 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
# 음.. 내 생각에는 답안 예시는 범위를 좁힐때 이진 탐색의 원리를 썼는데, 나는 그냥 O(N) 처럼 count 계속 올려서 찾은게 다른점?
# 위에 처럼 풀편 최대 10억 까지라서 정수임으로 순차 탐색은 분명 시간초과를 받는거지. 나 지금 순차 탐색으로 풀었음.
# 그리고 이제 이 문제에서는 현재 얻을 수 있는 떡볶이 양에 따라서 자를 위치를 결정해야 하기 때문에 이를 재귀적으로 구현하는 것은 귀찮은
# 작업이 될 수 있는거지, 그래서 이런 문제는 재귀적 X 반복문 이용해서 구현하면 더 간결하게 문제를 풀 수 있다.

# 답안 예시
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):  # start end 16 에서 한번더 돌고 if 먹고, result는 변함없으니까, 탈출가능 ㅇㅋ
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1   # end 16
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1  # 전번째 15

# 정답 출력
print(result)
