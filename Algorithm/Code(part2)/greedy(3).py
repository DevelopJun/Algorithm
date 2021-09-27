# # 문자열 뒤집기
#success
import time 
import math
from typing import final


start = time.time()
data = input()
result = 0

finala = 0

for i in range(len(data)-1):
    if(data[i] == data[i+1]):
        continue
    else:
        finala += 1  


if(finala % 2 == 0):
    print(finala // 2)
else:
    print((finala // 2)+1)

print("time :", time.time() - start)
# var = 5
# print(var%5)