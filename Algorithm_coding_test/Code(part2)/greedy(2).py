# 곱하기 혹은 더하기 
# success

S = input(str())
print(type(S))

L = list(S)
middle = []
for i in range(len(L)):
    middle.append(int(L[i]))

print(middle)
Final = 0
for l in range(len(L)):
    if(l == 0):
        Final += middle[l]
        continue
    if middle[l] == 0 or middle[l] == 1 or middle[l-1] == 0 or middle[l-1] == 1:
        Final += middle[l]
    else:
        Final = Final * middle[l]

print(Final)

# 모범 답안 코드  for 문 한번 시간복잡도 낮음
data = input()
result = int(data[0]) # data 형태가 str 인데, data[0] 이렇게 작성하면 str에서도 뽑을 수 있다.
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)