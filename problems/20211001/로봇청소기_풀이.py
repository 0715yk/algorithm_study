cases = int(input())

patterns = {
    1: {
        0: 2,
        1: 0,
        2: 3,
        3: 1
    },
    2: {
        0: 2,
        1: 3,
        2: 1,
        3: 0
    },
    3: {
        0: 1,
        1: 3,
        2: 0,
        3: 2
    },
    4: {
        0: 3,
        1: 2,
        2: 0,
        3: 1
    },
    5: {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }
}

for case in range(1, cases+1):
    n = int(input())
    board = []
    warps = {}
    start_point = []
    max_cnt = -1

    for i in range(n):
        input_list = list(map(int, input().split()))

        for idx, el in enumerate(input_list):
            if el == 0:
                start_point.append((i+1, idx+1))
            if el >= 6 and el <= 10:
                try:
                    prev = list(warps[el].keys())[0]
                    warps[el][(i+1, idx+1)] = prev
                    warps[el][prev] = (i+1, idx+1)
                except:
                    warps[el] = {}
                    warps[el][(i+1, idx+1)] = None

        board.append([5] + input_list + [5])

    limit_line = [[5 for i in range(n+2)]]
    board = limit_line + board + limit_line

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    patterns['warps'] = warps
    # 여기서부터 4방향으로 직진하는 while문을 만들어야함
    for start_dot in start_point:
        for way in range(4):
            path = set([start_dot])
            now_dot = start_dot
            now_way = way
            cnt = 0
            while True:
                cnt += 1
                if cnt > (n*n):
                    # 무한루프 방지 전체 맵수의 2배를 넘어가는 시행을 하면 끝내기
                    break
                now_value = board[now_dot[0]+dx[now_way]][now_dot[1]+dy[now_way]]
                now_dot = (now_dot[0]+dx[now_way], now_dot[1]+dy[now_way])

                if now_dot == start_dot and now_way == way:
                    if max_cnt < len(path):
                        max_cnt = len(path)
                    break

                if now_value >= 6 and now_value <= 10:
                    path.add(now_dot)
                    now_dot = patterns['warps'][now_value][now_dot]
                    path.add(now_dot)
                elif now_value >= 1 and now_value <= 5:
                    prev_way = now_way
                    now_way = patterns[now_value][now_way]
                    if now_value != 5 and abs(prev_way - now_way) != 2:
                        path.add(now_dot)
                elif now_value == -1:
                    if max_cnt < len(path):
                        max_cnt = len(path)
                    break
                elif now_value == 0:
                    path.add(now_dot)
                    
    print("#%s %s" % (case, max_cnt))
  