def solution(s):
    answer = 0
    arr = list(s)
    path = {}
    
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            l = arr[i:j]
            if len(l) == len(set(l)):
                try:
                    if path["".join(l)]:
                        continue
                except:
                    path["".join(l)] = True
                    answer += 1
    
    return answer


    # s는 중복이 있을 수 있음
    # 그러나 s의 부분 문자열은 중복이 없어야함(우선순위 1) 
    # 그리고 s의 부분 문자열이어야함
    # 좋은 부분 문자열의 개수를 구해라
    # 부분 문자열이 같을 경우 중복 카운트 x