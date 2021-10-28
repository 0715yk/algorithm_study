def solution(maps):
    answer = 0
    # maps에 대하여 경계처리 0으로 해줘야함
    # 시작점을 큐에 넣고
    # 끝점을 받아놓기
    strt = (1,1)
    end = (len(maps), len(maps[0])) 
    
    for idx in range(len(maps)):
        maps[idx] = [0] + maps[idx] + [0]
        
    limit_line = [[0 for i in range(end[1]+2)]]
    maps = limit_line + maps + limit_line
    queue = [strt]
    length = {}
    length[strt] = 1
    
    while len(queue) != 0:
        top = queue.pop(0)
        
        for way in [(top[0]-1,top[1]), (top[0],top[1]+1), (top[0]+1,top[1]), (top[0],top[1]-1)]:
            std = maps[way[0]][way[1]] 
            if std == 0:
                continue
            try:
                if isinstance(length[way],int):
                    continue
            except:
                if way[0] == end[0] and way[1] == end[1]:
                    # 도착한 것을 의미
                    return length[top] + 1 
                else:
                    # 아직 도착하지 못함

                    length[way] = length[top] + 1 
                    queue.append(way)
        
    return -1




