# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정 
# 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제 자주 출제, 
# 스택, 큐, 재귀함수

# 스택 예제

# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack)
# print(stack[::-1])

# 파이썬에서는 스택을 이용할 때에는 별도의 라이브러리 사용할 필요 x 
# append(), pop() 메서드 이용하면 된다. 

# 큐 예제
# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)

# 재귀함수 
# Recursive Function 자기 자신을 다시 호출하는 함수 

# def Recursive_Function():
#     print('재기 함수를 호출합니다.')
#     Recursive_Function()

# Recursive_Function()

# def Recursive_Function(i):
#     if i == 15:
#         return
#     print(i, '번쨰 재기 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
#     Recursive_Function(i + 1)
#     print(i, '번째 재귀함수를 종료 합니다.')

# Recursive_Function(1)

def factorial_iteractive(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1: # 여기서 만약에 if 문으로 n 조정 안하면 음수 나오거나, 무한루프 돌수도 있다는 거지. 
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iteractive(5))
print('재귀적으로 구현:', factorial_recursive(5))



