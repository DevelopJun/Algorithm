# 투 포인터를 최대한 활용한 방법 1

from abc import abstractproperty


inputdata = list(map(int, input().split()))


def trap(data: list[int]) -> int:
    print(data)
    if not data:
        return 0

    volume = 0
    left, right = 0, len(data) - 1
    left_max, right_max = data[left], data[right]

    # 제일 높은 부분 까지 결국 도달하면 while 문이 종료되는 것임.
    while left < right:
        left_max, right_max = max(data[left], left_max), max(
            data[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            # 이해!!!!!!!!!!) 여기서 volume이 움직이기 전 블록에서 움직인 후 블록이랑 차이를 이제 계산하는 부분임. 절대값이라고 생각하면 된다, max니까.
            volume += left_max - data[left]
            left += 1
            print("왼쪽이 오른쪽으로 이동")
        else:
            volume += right_max - data[right]
            right -= 1
            print("오른쪽이 왼쪽으로 이동")
        print('volume 변화값: ', volume)

    return volume


print("return 값", trap(inputdata))


# stack 스택 쌓기로 풀어본 방법

def trap2(data: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(data)):
        # 변곡점을 만나는 부분 , 이전 높이는 고정된 형태가 아니라 계속 바뀌니까,
        # 계속 스택으로 채워 나가다, 변곡점 만나면 스택에서 하나씩 꺼내면서
        while stack and data[i] > data[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(data[i], data[stack[-1]]) - data[top]

            volume += distance * waters

        stack.append(i)

    return volume


print('return 값', trap2(inputdata))
