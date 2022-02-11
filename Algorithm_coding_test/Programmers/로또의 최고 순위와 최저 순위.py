# 2021 DEV-Matching: 웹 백엔드 개발

def solution(lottos, win_nums):
    check = []
    unclear_number = []
    # 로또 당첨 내용
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for num in lottos:
        if num in win_nums:
            check.append(num)
        elif num == 0:
            unclear_number.append(num)

#     print('check', check)
#     print('unclear_number',unclear_number)

    # 최고 순위, 최저 순위
    answer = []
    # print('최고순위', dic[len(check) + len(unclear_number)])
    answer.append(dic[len(check) + len(unclear_number)])
    # print('최저 순위 ',dic[len(check)])
    answer.append(dic[len(check)])
    # print('answer', answer)

    return answer
