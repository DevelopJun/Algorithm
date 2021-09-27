# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

def solution(food_times , k):
    answer = 0
    ftime = len(food_times)
    i = ftime
    result = 0

    for _ in range(1, k + 1):
        if(food_times[ftime - i] != 0):
            food_times[ftime - i] -= 1
            i -= 1
            if(i == 0):
                i = ftime
            result = ftime - i 
        else:
            while(True):
                i -= 1
                if(i == 0):
                    i = ftime
                if(food_times[ftime - i] != 0):
                    food_times[ftime - i] -= 1
                    result = ftime - i
                    break
    
        print(food_times)
    if(result == len(food_times)-1):
        result = 1
    else:
        result += 1
        
    if(sum(food_times) == 0):
            answer = -1
            return answer
    else:
        answer = result
        return result

print(solution([3, 1, 2], 5))