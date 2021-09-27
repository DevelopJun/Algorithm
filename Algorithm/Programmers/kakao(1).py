# 카카오 키패드 누르기 인턴십
# 결국에는 풀었다.

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"


def solution(numbers, hand):
    pad = {1: 10, 2: 11, 3: 12, 4: 20, 5: 21, 6: 22, 7: 30,
           8: 31, 9: 32, '*': 40, 0: 41, '#': 42}
    left_point = pad['*']  # 40
    # print(left_point)
    right_point = pad['#']  # 42
    # print(right_point)
    answer = []

    for i in numbers:
        # print(i)
        if(i == 1 or i == 4 or i == 7):
            answer.append('L')
            left_point = pad[i]
        elif(i == 3 or i == 6 or i == 9):
            answer.append('R')
            right_point = pad[i]
        else:
            # 2580 비교하기
            left_distance = 3
            right_distance = 3
            if(left_point == pad[i]-10 or left_point == pad[i]+10 or left_point == pad[i]-1 or left_point == pad[i]+1):
                left_distance = 1
            if(left_point == pad[i]-11 or left_point == pad[i]-9 or left_point == pad[i]+9 or left_point == pad[i]+11):
                left_distance = 2
            if(right_point == pad[i]-10 or right_point == pad[i]+10 or right_point == pad[i]-1 or right_point == pad[i]+1):
                right_distance = 1
            if(right_point == pad[i]-11 or right_point == pad[i]-9 or right_point == pad[i]+9 or right_point == pad[i]+11):
                right_distance = 2

            if(left_distance == right_distance):
                if(hand == "right"):
                    answer.append('R')
                    right_point = pad[i]
                else:
                    answer.append('L')
                    left_point = pad[i]
            elif(left_distance > right_distance):
                answer.append('R')
                right_point = pad[i]

            elif(left_distance < right_distance):
                answer.append('L')
                left_point = pad[i]

    joined = "".join(answer)
    answer = joined
    return answer


print(solution(numbers, hand))
