'''
Counter 객체, 리스트 컴프리핸선
'''


import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# 지금 문자열을 보게 되면 쉼표랑 마침표 이런게 썩어져 있다. 따라서 전처리 과정
# pre processing이 필요한데 , 정규식을 사용해서 w는 정규식에서 문자를 뜻하고, ^ not 을 뜻한다
# 따라서 아래의 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환 하라는 역할
change = [word for word in re.sub(r'[^\w]', ' ', paragraph)
          .lower().split() if word not in banned]

print("****", change)
print(Counter(list(change)))
counter = Counter(change)

# 여기서 Counter을 반환 받을려면 most_common이라는 함수를 사용해야 한다.

print(counter.most_common(1))  # [('ball', 2)]
print(counter.most_common(1)[0][0])  # ball
