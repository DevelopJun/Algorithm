def get_request_count_during_one_second(time, start_and_end_times):
    request_count = 0
    start_time = time
    end_time = time + 1000

    for start_and_end_time in start_and_end_times:
        if start_and_end_time[1] >= start_time and start_and_end_time[0] < end_time:
            request_count += 1
    print("start_time", start_time, end_time, request_count)
    return request_count


def solution(lines):
    answer = 0
    # print(lines)
    start_and_end_times = []
    for line in lines:
        _, time, duration = line.split()
        time_array = time.split(':')
        duration = float(duration.replace('s', '')) * 1000  # micro
        end_time = (
            int(time_array[0]) * 3600 + int(time_array[1]) * 60 + float(time_array[2])) * 1000
        start_time = end_time - duration + 1
        start_and_end_times.append([start_time, end_time])

        print(start_and_end_times)

# 각 로그들의 시작되는 시점과 끝나는 시점을 기준으로 1초동안 얼마나 많은 로그가 포함되는가

    for start_and_end_time in start_and_end_times:
        answer = max(answer, get_request_count_during_one_second(start_and_end_time[0], start_and_end_times),
                     get_request_count_during_one_second(start_and_end_time[1], start_and_end_times))

    return answer
