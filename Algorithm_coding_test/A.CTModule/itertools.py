# itertools
# 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

# 이거는 이제 순서를 고려한
from itertools import product
from itertools import permutations
from itertools import combinations

# permutations
fruits = ['🍏', '🍌', '🍓']
result = list(permutations(fruits, 2))
# permutations 는 클래스라서 객체 초기화 이후에는 list로 변환하여 사용해야함.
# [('🍏', '🍌'), ('🍏', '🍓'), ('🍌', '🍏'), ('🍌', '🍓'), ('🍓', '🍏'), ('🍓', '🍌')]
print(result)

# combinations
# 이거는 이제 순서를 고려하지 않는 r 개의 데이트를 뽑는

fruits = ['🍏', '🍌', '🍓']
result = list(combinations(fruits, 2))

print(result)  # [('🍏', '🍌'), ('🍏', '🍓'), ('🍌', '🍓')]

# Prduct 이거는 중복 허용해서
fruits = ['🍏', '🍌', '🍓']
result = list(product(fruits, repeat=2))
# repeat: 중복 허용
# 만약 repeat을 써주지 않는다면 다음과 같은 에러가 발생한다.
# result = list(product(fruits, 2))
# TypeError: 'int' object is not iterable

# result [('🍏', '🍏'), ('🍏', '🍌'), ('🍏', '🍓'), ('🍌', '🍏'), ('🍌', '🍌'), ('🍌', '🍓'), ('🍓', '🍏'), ('🍓', '🍌'), ('🍓', '🍓')]
print(result)

##########################
