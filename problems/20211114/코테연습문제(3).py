def solution(s):
    answer = len(s)
    mid = len(s) // 2

    for i in range(1, mid+1):
        if len(s) % i != 0:
            continue
        prev = s[0:i]
        flag = True
    
        for j in range(i, len(s), i):
            if prev != s[j:j+i]:
                flag = False
                break
            else:
                continue
        if flag:
            if answer > i:
                answer = i
                break

    return answer

    # 문제에서 요구하는건 s 전체를 관통(?)하는 주기임
    # 즉, 반복되다가 말면 주기라고 안침
    # 그러면 더 쉽다 
    # 1, 2씩해보고, 3씩 해보고, 4......길이의 반까지?해보고 안되면 전체 길이 아닐까?
    # 여기에 전체를 지금 해보려는 문자열의 길이로 나눴을 때 안나눠떨어지면 고려할 필요x
    # 예를 들어, abababab 에서 aba 3개의 주기는 나올 수 없음. 
