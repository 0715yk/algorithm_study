# 풀이 1)
def solution(w,h):
    answer = None
    
    if w>h:
        a = w
        b = h
    else:
        a = h
        b = w
        
    while True:
        r = int(a % b)
        if r == 0:
            break
        a = b 
        b = r 
        
    answer = (h * w) - (h+w-b)
    
    return answer

import math

# 풀이 2)
def solution(w,h):
    answer = None
    
    b = math.gcd(w,h)
        
    answer = (h * w) - (h+w-b)
    
    return answer