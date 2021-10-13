answer = 0
result = 1
cnt = 0
def solution(clothes):
    global answer
    
    d = {}
    for el in clothes:
        try:
            d[el[1]].append(el[0])
        except:
            d[el[1]] = [el[0]]
    origin = len(clothes)
    clothes = list(d.keys())
    cases = len(clothes)
    
    if origin == cases :
        return (2**origin) - 1
    
    def get_cnt(depth, s=0):
        global result
        global answer
        global cnt 
        
        if cnt == depth:
            answer += result
            return

        for idx in range(s,len(clothes)):
            length = len(d[clothes[idx]])
            cnt+=1
            result*=length
            get_cnt(depth,idx+1)
            result//=length
            cnt -=1

    for i in range(1,cases+1):
        get_cnt(i)
        result = 1
    return answer


# 처음에 테케 1번이 시간초과나서.. 약간 편법으로 테케1번만 통과해서 푼문제인데 
# 다른 방법이 있었다.. 이걸 어떻게 생각해낼까??.

def solution(clothes):
    answer = 1
    d = {}
    
    for el in clothes:
        try:
            d[el[1]] += 1
        except:
            d[el[1]] = 1
    
    for key in list(d.keys()):
        answer *= (d[key]+1)
    
    return answer-1


#이렇게 심플해질수도 있었다는 것.
# 포인트는 경우의 수를 구할때 
# 나의 경우 입는 조합을 모두 카운트해야하므로 하나하나 다 셌지만
# 안입는 경우를 하나 더해놓으면 계산이 훨씬 편리해진다
# 이 생각하나가 코드를 완전히 바꿔놨다!