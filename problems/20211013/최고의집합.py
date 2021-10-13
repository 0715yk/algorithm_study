def solution(n, s):
    answer = []
    if s < n :
        return [-1]
    num = s//n
    l = [num for i in range(n)]
    if sum(l) == s:
        return l
    else:
        idx = 1
        sum_num = sum(l)
        while sum_num != s:
            l[-idx] += 1
            sum_num += 1
            idx+=1 
        return l
    