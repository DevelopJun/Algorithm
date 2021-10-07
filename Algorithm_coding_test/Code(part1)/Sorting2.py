# 성적이 낮은 순서로 학생 출력하기 준호 개인 코딩 풀이 

N = int(input())

array = []
number = []
for i in range(N):
    local = list(map(str, input().split()))
    array.append(local)
    number.append(int(array[i][1]))

number.sort()

for z in number:
    for l in array:
        if z == int(l[1]):
            print(l[0], end = ' ')

# 예시 답안 

n = int(input())

# N 명의 학생 정보를 입력받아 리스트에 저장 
array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))

# 키(key)를 이용하여, 점수를 기준으로 정렬 
array = sorted(array, key=lambda student: student[1]) # 이 lamda 유용하네, 잘 알고 있어야함, studnet 저 부분은 그냥 
# 변수라서 상관 없고, x : x[1] ㅇㅈㄹ 해도 괜찮은거임 진짜 꼭 외우자 

# 정렬이 수행된 결과를 출력 
for student in array:
    print(student[0], end=' ')
