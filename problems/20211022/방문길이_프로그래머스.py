def solution(dirs):
    answer = 0
    board = []
    for i in range(11):
        board.append([0]+[1 for j in range(11)]+[0])
        
    limit_line = [[0 for i in range(13)]]
    board = limit_line + board + limit_line
    now = (6,6)
    path = {}
    # 생각해보니 특정 좌표에서 특정 좌표로 갔다는 표시를 해둬야할 듯

    ways = {
        "U":0,
        "R":1,
        "D":2,
        "L":3
    }
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for way in dirs:
        next = (now[0] + dx[ways[way]], now[1] + dy[ways[way]])
        if board[next[0]][next[1]] == 0:
            continue
        else:
            try:
                if next in path[now] or now in path[next]:
                    now = next
                    continue
                else:
                    answer += 1 
                    path[now].add(next)
                    path[next].add(now)
                    now = next
            except:
                answer += 1 
                try:
                    if path[now]:
                        path[now].append(next)
                except:
                    path[now] = set([next])    
                    
                try:
                    if path[next]:
                        path[next].append(now)
                except:
                    path[next] = set([now])
                    
                now = next
            
    return answer


    # 11을 기준으로 만들어야함 점이니까
    # 일단 13*13 크기의 배열을 만든다. 이 때, 1은 경계처리용으로 만듦
    # 경계처리는 0으로 하고 나머지는 1로 한다
    # 명령에 따라 for문을 돌려서 움직이는데,
    # 만약에 다음 행선지가 0이면 해당 명령을 통과한다
    # 그리고 특정 영역을 밟을 때마다 path[좌표] = True 표시를 한다
    # 그래서 다음에 특정영역이 True인 곳을 밟으면 cnt +1 을 하지않는다.
    # 나머지는 밟을 때마다 cnt +1 
    # 그렇게 끝까지가서 끝나면 cnt를 리턴해주면 된다.



# 왜 오류가 나지??.... 도저히 모르겠음..

def solution(dirs):
    answer = 0
    board = []
    for i in range(11):
        board.append([0]+[1 for j in range(11)]+[0])
        
    limit_line = [[0 for i in range(13)]]
    board = limit_line + board + limit_line
    now = (6,6)
    path = set([])
    # 생각해보니 특정 좌표에서 특정 좌표로 갔다는 표시를 해둬야할 듯
    ways = {
        "U":0,
        "R":1,
        "D":2,
        "L":3
    }
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for way in dirs:
        next = (now[0] + dx[ways[way]], now[1] + dy[ways[way]])
        if board[next[0]][next[1]] == 0:
            continue
        else:
            path.add((now, next))
            path.add((next, now))
            now = next
        
    return len(path) // 2


# 생각해보니 이렇게 간단하게 풀수 있었음.. 