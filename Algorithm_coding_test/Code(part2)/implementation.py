
from os import rename
from typing import Deque
import re


class Implementaion:
    # 럭키 스트라이크
    def RuckyStrike(self, number: int) -> str:
        c = str(number)
        change = list(c)

        z = int(len(change) / 2)  # 반으로 나눈 첫번쨰 인덱스 z 값 설정

        # 앞뒤 분리함.
        front = change[:z]
        back = change[z:]

        # 리스트 안 문자열 바로 정수로 변환 가능한 방법 있나?
        front_initial_value = 0
        back_initial_value = 0
        for i in front:
            front_initial_value += int(i)
        for z in back:
            back_initial_value += int(z)
        if(front_initial_value == back_initial_value):
            return 'LUCKY'
        else:
            return 'READY'

    # 문자열 재 정렬
    def String_realignment(self, string: str) -> str:
        print(string)
        # numbers = re.sub(r'[^0-9]', '', string) 숫자만 빼낼려고 했으나. fiadall은 리스트로 바로 반환시켜주는 메소드라서 아래의 것을 사용하였다.
        numbers0 = re.findall(r'\d', string)
        str_list = (list(string))

        str_all_list = [word for word in str_list if word not in numbers0]
        str_all_list = sorted(str_all_list)

        numbers0 = [int(num) for num in numbers0]
        final_number = []

        x = ''.join(str_all_list)
        y = sum(numbers0)
        str_all_list.append(y)
        print('최종 리스트', str_all_list)
        final = [str(x) for x in str_all_list]
        final_final = ''.join(final)
        return final_final

    # 문자열 압축
    # https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

    def solution(self, s: str) -> int:
        answer = len(s)
        # 1개 단위 (step)부터 압축 단위를 늘러가며 확인
        for step in range(1, len(s) // 2 + 1):
            compressed = ''
            prev = s[0:step]  # 앞에서부터 step의 만큼의 문자열 추출
            count = 1
            # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
            for j in range(step, len(s), step):
                # 이전 상태와 동일하다면 압축 횟수(count) 증가
                if prev == s[j: j + step]:
                    count += 1
                # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
                else:
                    compressed += str(count) + prev if count >= 2 else prev
                    prev = s[j:j + step]
                    count = 1
            # 남 아있는 분자열에 대해서 처리
            compressed += str(count) + prev if count >= 2 else prev
            # 만들어지는 압축 문자열이 가장 짧은 것이 정답
            answer = min(answer, len(compressed))
        return answer

    def lock_key(self, l: list) -> bool:
        # 이해 못함
        pass

    def snake_apple(self):
        from collections import deque

        N = int(input())  # 보드 크기
        K = int(input())  # 사과 개수

        # NxN 의 board를 만든다.
        board_array = [[1]*(N+2)] + [[1] + [0]*N + [1]
                                     for _ in range(N)] + [[1]*(N+2)]
        print(board_array)

        for i in range(K):
            a, b = map(int, input().split())  # a, b : 사과 위치
            board_array[a][b] = 2  # 사과는 숫자 2로 표현

        L = int(input())  # 뱀의 방향 변환 횟수
        # 뱀의 방향 변환 정보
        L_array = list(map(lambda x: [int(x[0]), x[1]], [
                       input().split() for _ in range(L)]))

        time = 0  # 첫 시작은 0초부터
        x, y = 1, 1  # 뱀의 첫 위치
        direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0),
                     3: (0, -1)}  # 0:북, 1:동, 2:남, 3:서
        d = 1  # 현재 방향은 오른쪽 (동쪽)
        snake_array = deque([[1, 1]])  # 뱀의 위치를 큐로 나타낸다.

        # board_array -> 0: 빈공간, 1: 벽, 2: 사과, 3: 뱀
        board_array[1][1] = 3  # 처음 뱀이 (1, 1) 에 존재함으로

        # 이동한 후에 뱀 머리의 위치가 벽이거나, 자신의 몸일 경우 stop
        while(True):
            # 일단 뱀의 머리를 이동시킨다. 바라보고 있는 방향으로.
            x = x + direction[d][0]
            y = y + direction[d][1]

            # 이동한 곳에 사과가 있다.
            if board_array[x][y] == 2:
                board_array[x][y] = 3  # 이제는 사과 대신 뱀의 머리가 위치한다.
                # snake_array 의 맨 오른쪽 원소가 머리고, 왼쪽이 꼬리 부분이라서, 난중에 popleft 로 deque로 뺼려고,
                snake_array.append([x, y])
                time = time + 1
            # 이동한 곳에 사과가 없고, 그냥 빈 곤강이다.
            elif board_array[x][y] == 0:
                board_array[x][y] = 3
                snake_array.append([x, y])
                del_x, del_y = snake_array.popleft()  # 뱀의 전체 길이는 변하지 않아야 하기 때문에 꼬리를 제거
                board_array[del_x][del_y] = 0
                time = time + 1
            # 나머지는 이동한 위치가 벽(=1) 이거나 자신의 몸(=3) 이므로 stop
            else:
                time = time + 1
                break
            # 뱀의 방향 전화 정보
            if len(L_array) != 0:
                if L_array[0][0] == time:
                    if L_array[0][1] == 'L':  # 왼쪽으로 90도 회전
                        d = (d-1) % 4
                    elif L_array[0][1] == 'D':  # 오른쪽으로 90도 회전
                        d = (d+1) % 4
                    del L_array[0]  # 방향 전환했으므로 제거
        return time


implementation = Implementaion()
# print('Q 07 답', implementation.RuckyStrike(int(input())))
# print('Q o8 답', implementation.String_realignment(str(input())))
# print('Q o9 답', implementation.solution(str(input())))
print(implementation.snake_apple())
