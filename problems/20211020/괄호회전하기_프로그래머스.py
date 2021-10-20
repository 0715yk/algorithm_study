from collections import deque
right = {"()":True, "[]":True,"{}":True}
def solution(s):
    answer = 0
    # s를 0번~s-1번 회전시키면서 각각의 회전시에
    # 올바른 문자열인지 판단해서 몇개가 올바른 문자열인지 개수를 리턴
    # 1) 올바른 문자열인지 판단하는 함수 필요
    # 2) 회전시키는 로직이 필요
    # 회전시키는 로직은. .. deque rotate쓰자
    
    
    def check_right(arr):
        stack = []
        global right
        
        for el in arr:
            if len(stack) == 0:
                stack.append(el)
                continue
            else:
                top = stack[-1]
                try:
                    if right[top + el]:
                        stack.pop()    
                except:
                    stack.append(el)
                    
        if len(stack) == 0:
            return True
        else:
            return False
        
    d = deque(list(s))
    
    for i in range(0,len(s)):
        if check_right(list(d)):
            answer += 1
        d.rotate(-1)

    
    return answer