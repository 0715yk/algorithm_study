# 문제 : 크레인 인형 뽑기 게임(프로그래머스 level - 1 : 2019 카카오 개발자 겨울 인턴쉽 기출)
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    
    # 인덱싱 1부터 시작
    # 열을 기준으로 moves에서 인덱스를 받아서 해당 열의 맨 위에 것을 집는 것
    # 집어서 stack처럼 생긴 바구니에 넣음
    # 스택처럼 이란 말의 의미와 같이 맨위에것이랑 지금 넣으려는 숫자가 동일하면 pop
    # 동일하지 않으면 push 
    # 최종 사라진 인형의 개수는 pop을 할 때마다 카운팅해주기(2개씩 없어지니까 +2)
    
    # moves를 기준으로 for문을 만들고 - 1
    # board의 열을 기준으로(대신 move -1 인덱스로 처리하고)
    # 인형뽑기가 내려가는 것처럼 특정 열의 맨위에서 아래로 내려가다가 0이 아닌 숫자 마주치면 break 걸고 
    # 0으로 바꾸고, 바구니에 넣기(0이 아닌 숫자가 안나오면 그대로 끝남) -2
    # 바구니에 넣을 때 마지막 요소와 비교해서 같으면 마지막 요소 pop => answer +2 
    # 같지 않으면 그대로 push 
    basket = []
    
    for move in moves:
        idx = 0
        
        while idx < len(board):
            if board[idx][move-1] != 0:
                try:
                    if board[idx][move-1] == basket[-1]:
                        basket.pop()
                        answer += 2
                    else:
                        basket.append(board[idx][move-1])    
                except:
                    basket.append(board[idx][move-1])
                board[idx][move-1] = 0
                break
            else:
                idx += 1 
    
    return answer