def solution(n, times):
    maximum_time = max(times) * n 
    minimum_time = 1 
    answer = 0
    while minimum_time <= maximum_time:
        mid_time = (maximum_time + minimum_time) // 2
        people_cnt = 0
        
        for time in times:
            people_cnt += mid_time // time
            
        if people_cnt >= n :
            maximum_time = mid_time - 1 
            answer = mid_time
        elif people_cnt < n:
            minimum_time = mid_time + 1 
    return answer