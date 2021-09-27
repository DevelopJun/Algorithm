'''
코딩을 하다 보면 일단 코드의 전체 골격을 잡아 놓고 내부에서 처리할 내용은 차근차근
만들어야 하는 의도로 다음과 같이 코딩하는 경우가 있는데, 
클래스 에서는 함수 아래에 지정을 안해주면 인덴트 오류가 발생한다. 따라서 pass를 사용하여 이를 간단히 처리할 수 있다.
파이썬에서는 pass는 널 연산으로 아무것도 하지 않는 기능이다. 
'''


class MyCalss(object):
    def method_a(self):
        # 여기에 pass 추가
        pass

    def method_b(self):
        print("Method B")


c = MyCalss()
