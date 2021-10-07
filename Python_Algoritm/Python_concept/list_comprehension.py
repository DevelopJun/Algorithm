'''
파이썬은 map. filter와 같은 함수형 기능을 제공하며 다음과 같은 람다 표현식을 lambda expression 을 지원한다. 
lambda 는 일식적으로 쓰고 버리는 함수라고 생각하면 된다. 간단한 기능을 일반적인 함수와 같이 정의해두고 쓰는 것이 아니라 필요한 곳에서 쓰고 즉시 벌리 수 있다.
'''

list(map(lambda x: x + 10, [1, 2, 3]))

a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(a)

# 만약 리스트 컴프리 헨션을 사용하지 않으면 for 문으로 append로 조건문을 걸어 길게 풀어서 작성해야 한다.

a = {}
orginial = [1, 2]

for key, value in orginial.items():
    a[key] = value

a = {key: value for key, value in orginial.items()}

'''
위 처럼 한줄로 간결하게 작성할 수 있는 리스트 컴프리 헨션(딕셔너리 컴프리 헨션)은 가독성이 좋은 편이기 하지만, 
이 또한 무리하게 작성할 경우 가독성을 떨어 뜨릴 수 있으므로 적절히 사용하는게 중요하다. 

또한 리스트 컴프리헨션은 표현식이 2개를 넘지 않아야 한다. 여러 표현식을 여러 줄에 걸쳐 표현하면 가독성이 지나치게 떨어진다. 
'''
