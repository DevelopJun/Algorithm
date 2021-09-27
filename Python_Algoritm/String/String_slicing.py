'''
문자열 슬라이싱 (실행 시간 기준 빠른것)
1. 슬라이싱 => 1
2. 리스트 reverse => 5
3. reversed() + join() => 6
4. for 반복 => 12
5. while 반복 => 21
6. 재귀 => 54
'''


s = "안녕하세요"
print(s[1:4])  # 녕하세
print(s[1:-2])  # 녕하
print(s[1:])  # 녕하세요
print(s[:])  # 안녕하세요
print(s[1:100])  # 녕하세요
print(s[-1])  # 요
print(s[-4])  # 녕
print(s[:-3])  # 안녕
print(s[-3:])  # 하세요
print(s[::1])  # 안녕하세요
print(s[::-1])  # 요세하녕안
print(s[::2])  # 안하요
