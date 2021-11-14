answer = 1
path = {}
results = 1

def solution(board):
    global answer
    global path 
    global results 
    
    for idx, el in enumerate(board) :
        board[idx] = [0] + el + [0]
    limit_line = [[0 for i in range(6)]]
    board = limit_line + board + limit_line
    
    def DFS(top, std):
        global answer
        global path
        global results
        
        if results > answer:
            answer = results
            
        for way in [(top[0]-1,top[1]), (top[0],top[1]+1), (top[0]+1,top[1]), (top[0],top[1]-1)]:
            try:
                if path[way]:
                    continue
            except:
                path[way] = True
                if board[way[0]][way[1]] != std:
                    path[way] = True
                    continue
                results += 1
                DFS(way, std)
                results -= 1
        
    for i in range(1, 5):
        for j in range(1, 5):
            path[(i,j)] = True
            DFS((i,j), board[i][j])
            path = {}
            results = 1
    
    if answer == 1:
        answer = -1
        
    return answer


    # 각각의 숫자를 하나하나 (Board를) 탐색하면서
    # BFS를 한다음에 갈 수 있는 최대 길이 갱신해가면서 풀면될듯
    # 예외 사항 : 만약에 모두 1이다(2개이상 연결 불가다) 하면 -1 리턴
    # 1,2,3,4로만 이뤄져있다고함
    # board의 길이도 정해져있음 => DFS 아무리 시간복잡도 해봐야 16 * 16임
    # board의 좌표(인덱스)를 하나하나 기준으로 탐색
    # 그 좌표를 가지고 DFS 시작
    # BFS로 헀다가 망헀다 생각해보니 BFS로 하면 안됨... => DFS로 해야함
            
#         std = board[dot[0]][dot[1]]
#         queue = [dot]
#         path = {}
#         path[dot] = True
#         length = {}
#         length[dot] = 1
        
#         while len(queue) != 0:
#             top = queue.pop(0)

#             for way in [(top[0]-1,top[1]), (top[0],top[1]+1), (top[0]+1,top[1]), (top[0],top[1]-1)]:
#                 if board[way[0]][way[1]] == 0:
#                     continue
#                 try:
#                     if path[way]:
#                         continue
#                 except:
#                     if board[way[0]][way[1]] != std:
#                         path[way] = True
#                         continue
#                     path[way] = True
#                     length[way] = length[top] + 1
#                     if answer < length[top] + 1:
#                         answer = length[top] + 1
#                     queue.append(way)
    # 경계 처리해주자