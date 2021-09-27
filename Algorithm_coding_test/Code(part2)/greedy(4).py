# 만들 수 없는 금액 
# 100% 이해 못했음.
# 화폐 단위가 누적합보다 클 경우에는 두 숫자 사이에 갭이 있따는 뜻이므로, 
# 중간에 만들지 못하는 금액이 생기게 된다. 

import time 

N = input()
start = time.time()
list = list(map(int, input().split()))
list.sort()

target = 1
for x in list:
    # 만들 수 없는 금액을 찾았을 때 반복 종료 
    if target < x:
        break
    target += x # 신기하게도, 이렇게 덧샘을 하게 되면, 정말로 저 target 전까지는 다 만들 수 있음.
print(target)

print("time :", time.time() - start)