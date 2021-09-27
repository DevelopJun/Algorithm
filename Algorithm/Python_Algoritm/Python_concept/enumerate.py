'''
enumerate는 '열거하다'는 뜻의 함수로, 여러가지 자료형 (list, set, tuple)등의 인덱슬르 포함한 enumerate 객체로 리턴한다. 

'''

a = [1, 2, 3, 2, 45, 77, 3]
print(a)
print(enumerate(a))  # <enumerate object at 0x0000020A03BFB800>

# 이렇게 list()로 결과를 추출할 수 있는데, 인덱스를 자동을 지정해줘서 편리하게 사용할 수 있다.
print(list(enumerate(a)))

a = ['a1', 'b1', 'c1']

# 이렇게 사용하는 것 보다
for i in range(len(a)):
    print(i, a[i])

# 이렇게 사용하는 것이 가독성이 좋다.
for i, v in enumerate(a):
    print(i, v)
