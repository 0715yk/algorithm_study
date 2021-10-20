def solution(price, money, count):
    cnt = 1
    total = 0
    
    while cnt <= count:
        total+=price*cnt
        cnt+=1 
    answer = total-money
    
    if answer < 0:
        return 0
    else:
        return answer