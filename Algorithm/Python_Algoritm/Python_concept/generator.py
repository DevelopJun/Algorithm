'''
제너레이터는 루프의 반복 동작을 제어할 수 있는 루틴 형태이다. 
임이의 조건으로 숫자 1억개를 만드는 프로그램을 작성한다고 가정했을떄, 이 경우 제너레이터가 없다면 메모리 어딘가에 만들어낸 숫자 1억개를
보관해야 하는데, 이때 yield 구분을 사용하면 제너레이터를 리턴할 수 있다.

기존의 함수는 return 구문을 맞닥뜨리면 값을 리턴하고 모든 함수의 동작을 종료하는데, yield는 여기까지 실행중이던 값을 내보낸다는 의미로,
중간값을 리턴한 당므 함수는 종료되지 않는다. 
'''


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


print(get_natural_number())

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))  # 다음 값을 생성하려면 next()로 추출하면 된다.

# 제너레이터는 다음과 같이 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능하다.


def generator():
    yield 1
    yield 'String'
    yield True


g = generator()
print(next(g))
print(next(g))
print(next(g))
