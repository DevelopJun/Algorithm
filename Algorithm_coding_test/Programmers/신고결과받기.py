# 2020 kakao Blind  Recruitment
def solution(id_list, report, k):
    dic = {}
    check_dic = {}
    final_dic = {}
    # 딕셔너리 만드는 구조
    for i in range(len(id_list)):
        dic[id_list[i]] = []
        check_dic[id_list[i]] = 0
        final_dic[id_list[i]] = 0

    # print('dic ',dic)
    # print('check dic',check_dic)

    # 신고한 아이디와 정지된 아이디 정리
    for l in range(len(report)):
        extract = report[l].split()
        if extract[1] not in dic[extract[0]]:
            dic[extract[0]].append(extract[1])
            if extract[1] in check_dic:
                check_dic[extract[1]] += 1

    # print('dic', dic)
    # print('check dic',check_dic)

    answer = []
    for w in dic:
        for l in dic[w]:
            if check_dic[l] >= k:
                final_dic[w] += 1

    # print(dic[w], end=' ')
    # print(final_dic)

    answer = []
    for i in final_dic:
        answer.append(final_dic[i])
    return answer
