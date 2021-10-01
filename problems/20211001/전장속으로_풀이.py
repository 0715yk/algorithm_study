def BFS():
    global queue
    global board
    global lv 
    global level_candy
    global enemy_cnt
    
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    path = {}
    path[queue[0]] = True 
    length = 0
    prev_queue = [queue[0]]
    flag = False
    arr = []
    
    while True:
        length += 1 
        next_queue = []
        
        for top in prev_queue:
            for i in range(4):
                enemy = board[top[0]+dx[i]][top[1]+dy[i]]
                try:
                    if path[(top[0]+dx[i],top[1]+dy[i])]:
                        continue
                except:
                    pass
                if enemy > lv:
                    pass
                elif enemy == lv:
                    path[(top[0]+dx[i],top[1]+dy[i])] = True
                    next_queue.append((top[0]+dx[i],top[1]+dy[i]))
                elif enemy == 0:
                    path[(top[0]+dx[i],top[1]+dy[i])] = True
                    next_queue.append((top[0]+dx[i],top[1]+dy[i]))
                elif enemy < lv:
                    arr.append((top[0]+dx[i],top[1]+dy[i]))
                    flag = True

        prev_queue=[]
        
        if flag:
          arr.sort()
          board[arr[0][0]][arr[0][1]] = 0 
          queue = [arr[0]]
          enemy_cnt -= 1 
          return length
        else:
          prev_queue+= next_queue
          
        if len(prev_queue) == 0:
            return -1

cases = int(input())

for case in range(1,cases+1):
    n = int(input())
    board = []
    root = None 
    enemy_cnt = 0 
    
    for i in range(n):
        input_list = list(map(int, input().split()))
        for idx, el in enumerate(input_list):
            if el == 9:
                root = (i+1, idx+1)
                input_list[idx] = 0
            elif el >= 1 and el <= 8:
              enemy_cnt+= 1 
        board.append([100]+input_list+[100])
        
    limit_line = [[100 for i in range(n+2)]]
    board = limit_line + board + limit_line
    answer = 0
    lv = 2
    queue = [root]
    level_candy = 0
    
    while True:
        result = BFS()
        if result != -1:
            level_candy += 1 
            if level_candy == lv:
              level_candy = 0
              lv += 1 
            answer += result
        elif result == -1:
            print("#%s %s" % (case, answer))
            break
        
        if enemy_cnt <= 0:
            print("#%s %s" % (case, answer))
            break

    

