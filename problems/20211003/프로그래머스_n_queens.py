import copy 

def solution(n):
    answer = 0

    board = []

    for i in range(n):
        board.append([True for j in range(n)])

    def queens_road(copy_board, num) :
        checked = 1
        for i in range(n):
            for j in range(n):
                if not copy_board[i][j]:
                    continue
                elif copy_board[i][j] or num == (i,j):
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
        if checked >= n:
            return True 
        elif checked < n:
            return False
            
    for i in range(n):
        copy_board = copy.deepcopy(board)
        if queens_road(copy_board, (0,i)):
            answer +=1 

    return answer

## 2번째 풀이 


import copy 

cnt = 0
depth = 1
answer = 0
board = []

def solution(n):
    
    global board
    global depth
    global cnt 
    global answer

    for i in range(n):
        board.append([None]+[True for j in range(n)]+[None])
    board = [[None for i in range(n+2)]] + board + [[None for i in range(n+2)]]

    def queens_road(copy_board, num) :

        for k in range(1,n+1):
          if copy_board[k][num[1]] is not None:
            copy_board[k][num[1]] = False 
          else:
            break
        for k in range(1,n+1):
          if copy_board[num[0]+k][num[1]+k] is not None:
            copy_board[num[0]+k][num[1]+k] = False
          else:
            break
        for k in range(1,n+1):
          if copy_board[num[0]-k][num[1]+k] is not None:
            copy_board[num[0]-k][num[1]+k] = False
          else:
            break
        for k in range(1,n+1):
          if copy_board[num[0]+k][num[1]-k] is not None:
            copy_board[num[0]+k][num[1]-k] = False
          else:
            break
        for k in range(1,n+1):
          if copy_board[num[0]-k][num[1]-k] is not None:
            copy_board[num[0]-k][num[1]-k] = False
          else:
            break  

    # 재귀함수를 만들 것
    # 끝에가서 n번을 찍었는지를 체크해야함 
     
    limit_line = [[None for i in range(n+2)]]

    def recursion(arr) :
        global depth
        global cnt 
        global answer

        if cnt == n:
            answer += 1 
            return 
        
        for idx, el in enumerate(arr[depth]):
            if el is None:
                continue
            elif not el :
              continue
            elif el :
                copy_board = []

                for i in range(1,len(arr)-1):
                  new_arr = []
                  for j in range(1,len(arr)-1):
                    new_arr.append(arr[i][j])
                  copy_board.append([None]+new_arr+[None])
                copy_board =  limit_line + copy_board + limit_line

                queens_road(copy_board, (depth,idx))
                depth+=1 
                cnt+=1 
                recursion(copy_board)
                cnt-=1 
                depth-=1 


    recursion(board)
    return answer

print(solution(12))


# 마지막 시도!!
cnt = 0
depth = 0
answer = 0
col = set([])
way2 = set([])
way1 = set([])

def solution(n):

    global depth
    global cnt 
    global answer


    def recursion() :
        global depth
        global cnt 
        global answer
        global col
        global way1
        global way2

        if cnt == n:
            answer += 1 
            return 

        for idx in range(n):
              if idx in col or depth-idx in way2 or depth+idx in way1:
                continue
              else:
                col.add(idx)
                way1.add(depth+idx)
                way2.add(depth-idx)
              depth+=1 
              cnt+=1 
              recursion()
              depth-=1 
              cnt-=1 
              col.remove(idx)
              way1.remove(depth+idx)
              way2.remove(depth-idx)

        return answer
    
    return recursion()

    #clear