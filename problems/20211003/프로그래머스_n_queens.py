import copy 

def solution(n):
    answer = 0

    board = []

    for i in range(n):
        board.append([True for j in range(n)])

    # 그럼 여기서부터 board를 하나하나 탐색하는데 board의 x축의 mid까지만 탐색해도됨

    mid = n//2 

    for row in range(mid):
        for col in range(n):

            checked = 1
            board[row][col] = False
            copy_board = copy.deepcopy(board)

            for i in range(n):
                for j in range(n):
                    if not copy_board[i][j]:
                        continue
                    else:
                        checked += 1 
                        
                        for k in range(n):
                            copy_board[i][k] = False 
                        for k in range(n):
                            copy_board[k][j] = False 
                            
                        try:
                            for k in range(n):
                                copy_board[i+k][j+k] = False
                        except:
                            pass

                        try:
                            for k in range(n):
                                copy_board[i+k][j+k] = False
                        except:
                            pass
                        try:
                            for k in range(n):
                                copy_board[i-k][j+k] = False
                        except:
                            pass

                        try:
                            for k in range(n):
                                copy_board[i+k][j-k] = False
                        except:
                            pass
                            
                        try:
                            for k in range(n):
                                copy_board[i-k][j-k] = False
                        except:
                            pass



    return answer


