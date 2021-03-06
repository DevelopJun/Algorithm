a = 11
b = a
print(id(11), id(a), id(b))

b = 7
print(id(11), id(a), id(b))
'''
현재 위의 식을 보면 파이썬은 모든 것이 객체이므로 메모리 상에 위치한 객체의 주소를 얻어오는 id 함수를 실행한 결과는 놀랍게도 모두 동일하다. 
값을 담고 있는 변수는 사실 참조일 뿐이고, 실제로 값을 갖고 있는 int와 str은 모두 불변 객체이다. 

여기서 한가지 주의할 점은, C++ 참조(reference)와 파이썬의 참조 할당 방식은 조금 다르다. 
위를 보면 알겠지만, 현재 b의 값이 변경되었을때, 새로운 객체를 참조하게 되고, a는 변경되지 않고 그대로 유지된다.
'''
