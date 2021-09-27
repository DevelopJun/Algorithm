#3-2 답안 예시

n, m, k = map(int, input().split())

# N 개의 수 공백으로 구분하여 입력받기

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k  # 제일큰 값이 몇번 들어가는 확인하기 위해서 
count += m % (k+1) 

result = 0
result += (count) * first
result += (m-count) * second

print(result)
