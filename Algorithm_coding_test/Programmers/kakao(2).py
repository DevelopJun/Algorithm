# 신규 아이디 추천
# 정규 표현식

def solution(new_id):
    import re
    new_id1 = new_id.lower()  # 대문자 -> 소문자 변환
    new_id2 = ''.join(i for i in new_id1 if i.isalnum()
                      or i == '-' or i == '_' or i == '.')
    result = []
    result.append(new_id2[0])
    for i in range(1, len(new_id2)):
        if new_id2[i] == new_id2[i-1] and new_id2[i-1] == ".":
            continue
        else:
            result.append(new_id2[i])

    if result:
        if (result[0] == '.'):
            del result[0]

    if result:
        if (result[-1] == '.'):
            del result[-1]

    if not result:
        result.append("a")

    new_id5 = ''.join(result)

    new_id6 = ''
    if(len(new_id5) >= 16):
        new_id6 = new_id5[0:15]
        if(new_id6[-1] == '.'):
            new_id6 = new_id6[:-1]
    else:
        new_id6 = new_id5

    new_id7 = ''
    if(len(new_id6) <= 2):
        a = new_id6[-1]
        list_newid6 = list(new_id6)

        while(len(list_newid6) <= 2):
            list_newid6.append(a)

        new_id7 = ''.join(list_newid6)
        answer = new_id7
    else:
        answer = new_id6

    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))

# 정규 표현식을 배워야 한다.
# 정규 표현식이란 문자열의 규칙을 찾는 방법


def Goodanswer(new_id):
    import re
    st = new_id
    st = st.lower()  # 대문자 -> 소문자 변경
    st = re.sub('[^a-z\d\-_.]', '', st)  # 소문자, 숫자, 빼기, 및줄, 마침표 제외한 모든 문자를 제거
    st = re.sub('\.+', '.', st)  # 마침표 중복 제거
    st = re.sub('^[.]|[.]$', '', st)  # ^ 처음 $ 끝을 의미한다.
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])

    # 어쨌든 핵심은 정규표현식을 어떻게 작성하느냐,
    return st


print(Goodanswer("...!@Ba2T#*..y.abcdefghijklm"))
