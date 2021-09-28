# 원형 큐 디자인 방식
# 기존의 큐는 공간이 꽉차게 되면 더 이상 요소를 추가할 수 없었다. 심지어 앞쪽에 요소들이
# deQueue() 로 모두 빠져서 충분한 공간이 남게 되어도 그 쪽으로는 추가할 수 있는 방법이 없다. 그래서 앞쪽에 공간이 남아 있다면
# 동그라미 모형처럼 연결해 앞쪽으로 추가할 수 있도록 재활용 가능한 구조가 바로 원형 큐이다.

# 동작하는 원리는 투 포인터와도 비슷하다. 마지막 위치와

# rear 이 앞으로 처 나가는 아이, front가 뒤에서 따라 오는 아이
class CircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        # 이처럼 초기화 시에는 큐의 크기 k를 입력값으로 받는다. k 값은 당연히 최대 길이 maxlen이 되고, front 포인터는 p1정하고, rear 포인터는 p2로 정한다.
        pass

    def enQeue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
