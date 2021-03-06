'''
문자열 조작 String Manipulation은 문자열을 분리하거나 변경하는 등의 여러 과정에서 말한다.
원래 문자열은 로우 레벨에서 조작하거나, C 처럼 문자형이 따로 없는 언어에서는 조작이 매우 까다롭다. 
하지만 대부분의 언어에서 지원하고, 실무에서 가장 많이 사용하는 분야임이다.

1. 정보처리분야: 어떤 키워드로 웹 페이지를 탐색할때 문자열 처리 애플리케이션을 이용하게 된다. 특히 현대의 거의 모든 정보는
문자열로 구성되어 있으며, 문자열 처리는 정보 처리에 핵심적인 역할을 한다. 

2. 통신 시스템 분야: 문자 메세지나 이메일을 보낼 때 기본적으로 문자열을 어느 한 곳에서 다른 곳으로 보내게 된다. 이처럼 데이터 전송은 문자열
처리 알고리즘이 탄생한 기원이다. 데이터 전송에서 문자열 처리 매우 중요하다.

3. 프로그래밍 시스템 분야: 프로그램은 그 자체가 문자열로 구성되어 있따. 컴파일러나 인터프리터 등의 문자열을 해석하고 처리하여 기계어로
변환하는 역할을 하며, 여기에 정교한 처리 알고리즘이 쓰인다.
'''

'''
정규식 정리[매우 중요]
'''

# 모듈 임포트 이후에

# (1) 컴파일 후 매칭
import re
pattern = re.compile("apple")
print(pattern)
x = pattern.search("I like apple!")
print(x)
# (2) 축약형
x = re.search("apple", "I like apple!")

# 메타 문자(Meta characters) -> 메타 문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
'''
[]
이것은 문자열 클래스로, [] 사이의 문자들 중 하나와 매치 
하이픈으로 연결 가능 ([0-9], [a-z])
[^ ] 시작할 경우 반대 의미 
.(dot)

'''

'''
정규식 메서드
pattern 객체의 메세드 

'''
