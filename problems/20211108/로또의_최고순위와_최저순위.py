def solution(lottos, win_nums):
    answer = []
    
    collect_cnt = len(set(lottos) & set(win_nums))-1
    
    price = [6, 5, 4, 3, 2, 1, 6]
    
    answer.append(price[collect_cnt+ lottos.count(0)])
    answer.append(price[collect_cnt])
    
    return answer


    # 최고 순위와 최저 순위를 구하는 문제
    # 먼저, 최저 순위는 맞춘 개수를 고려한다음에 생각해야함
    # 예를 들어, 이미 2개를 맞췄다면 아무리 조작을가해도 5등이 최소임
    # 결론적으로 최소순위는 맞춘 개수임.
        
    # 최고 순위는 일단 맞춘 개수에서
    # 0을 가지고 조작을 가해야함
    # 맞춘 개수 + 0의 개수 