import copy
import sys 
sys.setrecursionlimit(1000000)

result = []
answer = []

def get(arr, num):
    global result
    global answer
    
    if sum(result) == num:
        result.sort()
        if result not in answer:
            answer.append(result[:])
        return 
    elif sum(result) > num:
        return 
    
    for el in arr:
        result.append(el)
        get(arr, num)
        result.pop()
        
def solution(n, money):
    global answer
    money.sort()
    if money[0] > n:
        return 0
    elif money[0] == n:
        return 1
    else:
        strt = money[0]
        first = 1 
        get(money[:3], first+1)
        second = len(answer)
        answer = []
        get(money[:3], first+2)
        third = len(answer)
        idx = 3
        now = None
        while idx != n:
            now = (first % 1000000007) + (second % 1000000007)
            first = second % 1000000007
            second = third % 1000000007
            third = now % 1000000007
            
            idx += 1 
            
        return now % 1000000007
    
    # [ 1, 2, 5]
    # 1
    # 1 
    # = 1
    # 2
    # 1,1 
    # 2
    # = 2
    # 3
    # 1,1,1
    # 1,2
    # = 2 
    # 4
    # 1,1,1,1
    # 1,1,2
    # 2,2
    # = 3
    # 5
    # 1,1,1,1,1
    # 1,1,1,2
    # 1,2,2
    # 5
    # = 4
    # 6
    # 1,1,1,1,1,1
    # 1,1,1,1,2
    # 1,1,2,2
    # 2,2,2
    # 1,5
    # = 5 
    # 1,2,2,3,4,5
    
    # = 2
    # 5 
    # 1,2,3,4,5 
    # 1 * 5
    # 2 *1 + 3*1  
    # 4*1 + 1*1 
    # 5*1 
    
    # 6 
    # [1,3,5]
    
    # 1
    # = 1
    # 2
    # 1,1
    # = 1 
    # 3 
    # 1,1,1
    # 3
    # = 2
    # 4
    # 1,1,1,1
    # 1,3 
    # = 2
    # 5 
    # 1,1,1,1,1
    # 1,1,3
    # 5
    # = 3 
    # 6
    # 1,1,1,1,1,1
    # 1,1,1,3
    # 3,3
    # 1,5
    # = 4
    # 1,1,2,2,3,4
    # 2,2,2
    # 4,2
    # 3,3,3,
    # 3,5,5,
    # 5,5 
    
    # 3번째까지 구하면 그 뒤부터는 한칸씩 띄는 피보나치
    # 일단 세번째까지는 구해야함 (n보다 작으면서 1부터 3번쨰)

# DP문제라는데.. 나는 답을 못찾았다.. 다시 풀어보기!