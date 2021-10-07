'''
제너레이터 방식을 활용하는 대표적인 함수로 range() 가 있다.

'''
import sys

print(list(range(5)))  # [0, 1, 2, 3, 4]
print(type(range(5)))  # <class 'range'>

# 여기서 range()는 range 클래스를 리턴하며, for 문에서 사용할 경우 내부적으로는 제너레이터 next()를 호출하듯 매번 다음 숫자를 생성해낸다.

a = [n for n in range(100000)]
b = range(100000)

print(len(a))
print(len(b))
print(len(a) == len(b))  # True

print(sys.getsizeof(a))  # 800984
print(sys.getsizeof(b))  # 48

# a 는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재한다.
# 둘 사이의 메모리 점유율 비교해보면 현재 확실히 차이나는 것을 볼 수 있는데, 생성 조건만 보관하기 때문에
