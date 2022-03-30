# 입국 심사 #

def solution(n, times):

    # 최악의 경우: 가장 비효율적인 심사관에게 다 받은 경우의 시간
    left, right = 1, max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        people = 0
        for i in times:
            # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
            people += mid // i
            # 모든 사람을 심사할 수 있으면 반복문을 벗어난다.
            if people >= n:
                break

        # 모든 사람을 심사할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다
        if people >= n:
            answer = mid
            right = mid - 1
        # 모든 사람을 심사할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        elif people < n:
            left = mid + 1

    return answer


# 전체적으로 이분탐색을 어떻게 진행해야 되는지 감이 오지 않았던 문제,
# 한 심사관에게 다 받은 경우의 시간을 최악으로 넣고,
# left, right 시간을 조정해가면서, 과연 각 심사관 마다 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지,
# 그리고 이 사람의 심사가 가능하다면 반복문 벗어나게 해서, 하나씩 좁혀 나가면서 확인하는 절차를 가지는거임.
