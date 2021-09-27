# Collections
# deque, counter 등 유용한 자료구조를 제공하는 표준 라이브러리

# deque: 양쪽 끝에서 빠르게 추가(append)와 삭제(pop)을 할 수 있는 리스트류 컨테이너
# Counter: hashable object를 세는 데 사용하는 딕셔너리 서브 클래스, elemnet는 dictionary key로 저장되고,
# 개수는 dictionary value로 저장된다.


##############################################
from collections import Counter
from collections import deque

a = deque([1, 2, 3, 3, 3, 5, 5, 7])
a.appendleft(9)
a.append(10)

print(list(a))  # result [9, 1, 2, 3, 3, 3, 5, 5, 7, 10]


###############################################

counter = Counter(['🍍', '🍎', '🍍', '🍇', '🍎', '🍎', '🍍', '🍎'])

print(counter)  # Counter({'🍎': 4, '🍍': 3, '🍇': 1})
print(counter['🍍'])  # 3
print(counter['🍎'])  # 4
print(counter['🍇'])  # 1
print(dict(counter))  # {'🍍': 3, '🍎': 4, '🍇': 1}

###############################################
