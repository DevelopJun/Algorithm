# 괄호로 된 입력값이 올바른지 판별하라

class stack:
    def valid_parentheses(self, list: list[str]) -> True:
        print(list)
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in list:
            if char not in table:
                stack.append(char)
                print(stack)
            elif table[char] != stack.pop():
                return False
            elif stack:
                stack.pop()

        return len(stack) == 0


inputdata = list(str(input()))
# print(list(inputdata))
Stack = stack()  # 이렇게 class를 인스턴스화 시키지 않고 실행하면 에러가 발생한다. 이 처럼 인스턴스화(instaniate)
print(Stack.valid_parentheses(inputdata))
