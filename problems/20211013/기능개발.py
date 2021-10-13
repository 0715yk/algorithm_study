def solution(progresses, speeds):
    answer = []
    d = {}
    prev = -1 
    
    for idx,p in enumerate(progresses):
        num = (100 - p)//speeds[idx] 
        if (100 - p)%speeds[idx] != 0:
            num += 1 
        if prev >= num:
           d[prev].append(num)
        else:
            d[num] = []
            prev = num
    for key,val in d.items():
        answer.append(len(val)+1)
    return answer