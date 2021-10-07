# 럭키 스트레이트


from typing import Deque
import re


class Implementaion:
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


implementation = Implementaion()
# print('Q 07 답', implementation.RuckyStrike(int(input())))
# print('Q o8 답', implementation.String_realignment(str(input())))
print('Q o8 답', implementation.String_realignment(str(input())))
