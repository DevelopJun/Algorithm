# from hashlib import new
# import random  # 랜덤 모듈 생성


# list = []  # 각 게임마다 몇번 만에 숫자르 맞추었는지 기록 하는 곳


# for i in range(1, 6):
#     count = 0  # 매 게임마다 몇번 만에 숫자를 맞추ㄴ었는지 기록하는 변수
#     print("###########", i, "번째 문제입니다. ############")
#     a = random.randint(1, 10)  # a 라는 변수에 1부터 50까지 랜덤 난수(정수) 생성
#     b = int(input())  # 플레이어가 추측해서 입력한 숫자

#     while a != b and count < 4:
#         count += 1
#         if a > b:
#             print("입력하신 숫자가 문제 정답보다 낮습니다.")
#             c = int(input())
#             b = int(c)
#         else:
#             print("입력하신 숫자가 문제 정답보다 큽니다.")
#             c = int(input())
#             b = int(c)

#     if a == b:
#         print("맞았습니다.")
#         list.append(count)  # 매 게임마다 몇 번 만에 숫자를 맞추었는지 기록
#     else:
#         print("결국 못 맞췄습니다.")

# print("전 게임을 통틀어 몇 번 만에 숫자를 맞추었는지 평균값은 ", sum(list)/len(list), "입니다.")


# def convert_to_fahrenheit(celsius):
#     a = ((celsius * 9/5) + 32)
#     return int(a)


# print("섭씨 온도(C)를 입력하세요 :")
# temperature = int(input())

# c = convert_to_fahrenheit(temperature)
# print("변화된 화씨(F) 온도 :", c)
