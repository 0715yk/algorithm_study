def solution(d, budget):
    answer = 0
    # 최대로 지원하는 케이스를 구해라
    # 가장 적게 지원금을 요청한 케이스 순서대로 들어주면(?) 
    # 최대로 많은 수의 부서에 지원할 수 있음
    d.sort()
    # 먼저 오름차순 정렬하고
    # budget을 바탕으로 지원 시작!0이될 때까지
    for el in d:
        budget-=el
        answer += 1 
        if budget == 0:
            return answer
        elif budget < 0:
            return answer - 1
        else:
            continue
            
    return answer