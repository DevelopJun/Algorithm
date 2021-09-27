# 왕실의 나이트(준호 개인 풀이)
location = str(input())
local = list(location)

rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

count = 1

for row in rows:
    if row == local[0]:
        x = count 
    count += 1

y = int(local[1])

steps = [(-2, 1),(-2, -1),(2, -1),(2, 1),(1, 2),(1, -2),(-1, -2),(-1, 2)]

result = 0

for step in steps:
    if 0 < step[0] + int(x) <= 8 and 0 < step[1] + int(y) <= 8:
        result += 1

print(result)

# 왕실의 나이트(4-3.py 답안 예시)
input_data = input()
row = int(input_data[1]) # 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키 코드로 a 를 숫자로 바꾼거임..sibal

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)




