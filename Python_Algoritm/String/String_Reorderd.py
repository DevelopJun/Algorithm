'''
로그 파일 재 정렬 

람다 표현식이란? -> 
람다 표현식이란 식별자 없이 실행 가능한 함수를 말하며, 함수  선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있다. 

'''
from typing import List


class Solution:
    def reorderLogFiles(logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


logs = ["dig 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

print(Solution.reorderLogFiles(logs))
