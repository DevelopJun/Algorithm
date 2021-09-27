# 프로그래머스 기능개발 

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]




def solution(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        load = 0
        while(progresses[i] < 100):
            progresses[i] += speeds[i]
            load += 1
        result.append(load)

    answer = []
    while(result[0] != None):
        l = 1
        z = 0
        while(result[0] > result[l]):
                l += 1 
                z += 1
                if ( l >= len(result)):
                    break

        head = 0
        for _ in range(l):
            result.pop(0)
            head += 1


        answer.append(head)
        if(len(result) == 1):
            answer.append(1)
            result.pop(0)
            break

        if(len(result) == 0):
            break
        

    return answer


print(solution(progresses, speeds))

