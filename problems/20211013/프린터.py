def solution(priorities, location):
    cnt = 0
    while True:
        top = priorities.pop(0)
        try:
            if max(priorities):
                pass
        except:
            return cnt+1
        if top >= max(priorities):
            # 출력
            cnt += 1 
            if location == 0:
                return cnt 
            else:
                pass
        else:
            priorities.append(top)
        location -= 1
        if location < 0 :
            location += len(priorities) 
    
# priorities의 원소들을 하나씩 pop(0) 하면서 진행
# while 문을 써서 진행
# 이 때, top 이 나머지 배열의 max보다 크거나 같으면 그대로 출력하는데
# 이 때, 그 인덱스가 location과 같으면 return 정답
# 안같으면 pass 함
# 반대로 top이 나머지 배열의 max보다 작다? 
# 다시 append()함 끝에
# 그리고 두 경우 모두다 location -=1 씩해줌
# 이 때, location이 음수면 전체 길이에 더해줌