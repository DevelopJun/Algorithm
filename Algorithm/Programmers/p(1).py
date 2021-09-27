# 짝지어 제거하기 
# 프로그래머스에서는 문자열을 그대로 넣어주고 알고리즘만 삽입하는 형태 

def solution(s):
    s = list(S)
    i = 0
    if(s == None):
        print("비어 있습니다")
        return 0
    else:
        while(True):
            if(s[i] == s[i+1]):
                s.pop(i)
                s.pop(i) # del 방법과 어떤 것이 더 빠른가? 
                i = 0
                if not s:
                    return print(1)
                    break
            else:
                i += 1
                if(i >= len(s)-1):
                    return print(0)
                    break


# 이렇게 stack 으로 pop 형태로 만들어서 할 수 도 있다. 
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0
