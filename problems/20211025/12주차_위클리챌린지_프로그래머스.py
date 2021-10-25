import math 
answer = 0

def recursion(arr,k, cnt) :
    global answer 
    
    if len(arr) == 0:
        answer = cnt
        return True
    else:
        if answer < cnt - len(arr):
            answer = cnt - len(arr)
            
    for idx, el in enumerate(arr):
        if el[0] > k:
            continue
        else:  
            k -= el[1]
            del arr[idx]
            if recursion(arr,k,cnt):
                return True
            arr.insert(idx,el)
            k += el[1]
            
def solution(k, dungeons):
    global answer 
    recursion(dungeons,k,len(dungeons))
    return answer


    # 최소 피로도가 있기 때문에 높은 곳부터 도는것이 유리할 수도 있음.
    # 근데 또 그 최소 피로도가 높은 곳의 소모피로도가 높으면 불리할수도 있음
    # 던전수 어차피 8개 이하고,
    # 전부다 탐색?? 8!??
    # 완전탐색으로 탐색하면서 
    # 만약에 최소 피로도의 기준에 부적합하면 그쪽은 짤
    # 적합하면 계속 탐색
    # 그렇게 계속 가다가 짤되는 순간에 max 갱신
    # 그렇게 전부 탐색했을 때 max값을 구하면 됨