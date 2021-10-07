# 입력 : "cbacdcbc"
# 츨력 : "acdb"

from typing import Collection, Counter, Set


class Stack:

    def removeduplicate(self, s: str) -> str:
        from collections import Counter
        # 집합으로 정렬
        Counter, seen, stack = Counter(s), set(), []

        for char in s:
            Counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and char < stack[-1] and Counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


stack = Stack()
print(stack.removeduplicate("cbacdcbc"))
