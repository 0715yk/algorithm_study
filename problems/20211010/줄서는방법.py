answer = []
cnt = 0

def recursion(arr,n,k):
    global answer
    global cnt 
    
    if len(answer) == n:
        cnt += 1 
        if cnt == k:
            return True
        else:
            return False
    
    for idx,el in enumerate(arr):
        if el in answer:
            continue
        else:
            answer.append(el)
            arr.remove(el)
            if recursion(arr,n,k):
                return True
            arr.insert(idx,el)
            answer.pop()
            
def solution(n, k):
    global answer
    
    arr = [i for i in range(1,n+1)]
    recursion(arr, n,k)
    
    return answer
    
# 완전탐색으로는 못구함
# 시간복잡도가 20!이라서 안됨...
# 그러면 이미 몇번째인지를 알고 있으니까
# 예를 들어, 예시의 경우 6개중에 5번째라했으니까
# 1로 만들수있는 2개, 2로 만들 수 있는 2개는 버리고 계산가능
# 즉 3으로 시작하는 조합 안에 있을 것임을 알 수 있음
# 이런식으로 수를 줄이고 시작해야할 것 같다.

answer = []
cnt = 0
r = []
def factorial(num):
    if num == 1:
        return 1 
    if num == 0:
        return 0
    else:
        return num * factorial(num-1)
    
def recursion(arr,n,k):
    global answer
    global cnt 
    global r

    if len(answer) == n-1:
        answer.append(arr[0])
        r.append(answer[:])
        answer.pop()
        return 
    #[1,2,3,4]
    std = factorial(len(arr)-1)
    minus_cnt = 0
    for idx, el in enumerate(arr):
        if k > el * std:
            minus_cnt += 1
            continue
        if el in answer:
            continue
        else:
            k -= minus_cnt * std
            answer.append(el)
            arr.remove(el)
            recursion(arr,n,k)
            arr.insert(idx,el)
            answer.pop()
            
def solution(n, k):
    global answer
    global r
    arr = [i for i in range(1,n+1)]
    recursion(arr, n,k)
    print(r)
    return answer

# 어떻게 될 것 같았으나.. 실패..!

