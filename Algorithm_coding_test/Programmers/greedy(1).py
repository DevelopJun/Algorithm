def solution(n, lost, reserve):
    pre = [0 * i for i in range(n)]

    members = [[v, i+1] for i, v in enumerate(pre)]
   # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다. 라는 가정 예외처리 해야함.
    for z in reserve:
        members[z-1][0] = 1
    for l in lost:
        if members[l-1][0] == 1:
            members[l-1][0] = 0
        else:
            members[l-1][0] = -1

    for i in range(n-2):
        if members[i+1][0] == -1 and members[i][0] == 1:
            members[i][0] = 0
            members[i+1][0] = 0
        if members[i+1][0] == -1 and members[i+2][0] == 1:
            members[i+2][0] = 0
            members[i+1][0] = 0

    final = [i for i in range(n) if members[i][0] >= 0]

    answer = len(final)
    return answer

# 위에 정확도 75%에서 계속 통과가 안되어서, 처리하지 못함, 결국 답 봄.


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


# 정답을 넣었는데도 정확도가 올라가지 않음. 아마 이건 내가 푼거라고 생각 해야할듯,. 하지만 이 사람들처럼
# 좀 간결하게 더 코딩할 필요가 있다고 생각함.

def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve)

    for reserve_person in reserve_set:
        if reserve_person-1 in lost_set:
            lost_set.remove(reserve_person-1)
        elif reserve_person+1 in lost_set:
            lost_set.remove(reserve_person+1)

    return n-len(lost_set)

# 아마 중복을 위에는 제거를 안해서 그런 것 같다,.
