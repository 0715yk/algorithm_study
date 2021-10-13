def solution(genres, plays):
    answer = []
    a = {}
    b = {}
    for i in range(len(genres)):
        try:
            a[genres[i]]+=plays[i]
        except:
            a[genres[i]] = plays[i]
            
        try:
            b[genres[i]].append(plays[i])
        except:
            b[genres[i]] = [plays[i]]
            
    new_a = {}
    
    for key, val in a.items():
        new_a[val] = key
    a = []
    for key in sorted(new_a, reverse=True):
        a.append(new_a[key])
        
    for gen in a:
        b[gen].sort(reverse=True)
        result = b[gen]
        for el in result[:2]:
            idx = plays.index(el)
            answer.append(idx)
            plays[idx] = None
        
    return answer