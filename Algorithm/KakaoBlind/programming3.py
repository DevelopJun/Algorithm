import math
from operator import itemgetter


def solution(fees, records):
    mangage = {}
    for i in records:
        if int(i.split()[1]) in mangage:
            mangage[int(i.split()[1])].append(i.split()[0])
            mangage[int(i.split()[1])].append(i.split()[2])
        else:
            mangage[int(i.split()[1])] = [i.split()[0], i.split()[2]]

    print(mangage)
    mangage1 = sorted(mangage.items(), key=itemgetter(0))
    print("제발 ", mangage1)
    mangage1 = dict(mangage1)
    timecalculate = []
    for key, value in mangage1.items():

        print("각 차의 정보 ", key, value)
        if len(value) % 4 == 0:  # 홀수라면
            print("출차 했음")
            counta = []
            timeM = 0
            for i in range(len(value) // 2):
                counta.append(value[i * 2])
                if len(counta) == 2:
                    kaki = int(counta[1][0:2]) - int(counta[0][0:2])
                    kako = int(counta[1][3:5]) - int(counta[0][3:5])
                    kaki = kaki * 60
                    time = kaki + kako
                    timeM += time
                    counta = []

            print("모든 시간 ", timeM)

            if int(timeM) <= int(fees[0]):
                timecalculate.append(fees[1])
            else:
                # 식 작성
                timecalculate.append(
                    fees[1] + (math.ceil((timeM - fees[0]) / 10)) * 600)

            print("dfdfsfsd", timecalculate)
        else:  # 짝수라면
            print("출차 안했음")

            countb = []
            timeM = 0
            for i in range(len(value) // 2):
                countb.append(value[i * 2])

                if len(countb) == 2 and i != (len(value) // 2):
                    kaki = int(countb[1][0:2]) - int(countb[0][0:2])
                    kako = int(countb[1][3:5]) - int(countb[0][3:5])
                    kaki = kaki * 60
                    time = kaki + kako
                    timeM += time
                    countb = []
                elif i != 0:
                    kaki = int(23) - int(countb[0][0:2])
                    kako = int(59) - int(countb[0][3:5])
                    kaki = kaki * 60
                    time = kaki + kako
                    timeM += time
                    countb = []
                print(timeM)

            print("모든 시간 ", timeM)
            if timeM <= fees[0]:
                timecalculate.append(fees[1])
            else:
                # 식 작성
                timecalculate.append(
                    fees[1] + (math.ceil((timeM - fees[0]) / 10)) * 600)

            print("dfdfsfsd", timecalculate)

            print('*' * 50)

    print(timecalculate)
    answer = []
    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
         "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
