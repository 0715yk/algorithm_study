# import copy


# def search_area(dot, board):
#     global power

#     queue = []
#     board[dot[0]][dot[1]] = 0

#     d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#     for el in d:
#         x = dot[0] + el[0]
#         y = dot[1] + el[1]

#         for i in range(power[dot]):
#             if board[x][y] == -1:
#                 break
#             elif board[x][y] != 0:
#                 queue.append((x, y))
#             x += el[0]
#             y += el[1]

#         return [queue, board]


# def get_left(board):
#     cnt = 0
#     new_queue = []
#     for i in range(1, len(board)-1):
#         for j in range(1, len(board)-1):
#             if board[i][j] != 0 and board[i][j] != -1:
#                 new_queue.append((i, j))
#                 cnt += 1
#     return [cnt, new_queue]


# def BFS(root, board):
#     copy_board = copy.deepcopy(board)
#     queue = [root]

#     while len(queue) != 0:
#         top = queue.pop(0)
#         if copy_board[top[0]][top[1]] == 0:
#             continue
#         [next_queue, next_copy_board] = search_area(top, copy_board)
#         queue += next_queue
#         copy_board = next_copy_board

#     [left, new_queue] = get_left(copy_board)

#     if left == 0:
#         return 0
#     else:
#         return {
#             'left': left,
#             'board': copy_board,
#             'queue': new_queue
#         }


# k = 3


# def get_result(board, queue):
#     # 처음 board를 가지고, queue를 뽑아내고 여기에 매개변수로 주면
#     # 예를 들어 최대 15개의 좌표값을 가지고 BFS를 돌리는 것
#     # 그 중 가장 적게 left를 가진것
#     # 만약 left가 0인 것이 있다면 그대로 print(0)
#     # 가장 적게 left를 가진 것의 queue를 다음 get_result의 매개변수로 줘야함
#     # copy_board도
#     min_left = 20

#     for dot in queue:
#         result = BFS(dot, board)

#         if result == 0:
#             return 0
#         else:
#             if result['left'] < min_left:
#                 min_left = result['left']
#                 min_board = result['board']
#                 min_queue = result['queue']

#     return [min_board, min_queue]


# answer = 0
# k -= 1
# case = 1

# if k < 0:
#     answer += 1
# if get_result() == 0:
#     if k >= 0:
#         print("#%s %s" % (case, 0))
#     else:
#         print("#%s %s" % (case, answer))
# else:
#     # board, queue 갱신 후 다시 get_result

# n, m, k = map(int, input().split())

# board = []
# power = {}
# queue = []

# for i in range(n):
#     input_list = list(map(int, input().split()))
#     for j, val in enumerate(input_list):
#         if val != 0:
#             queue.append((i+1, j+1))
#             power[(i+1, j+1)] = val
#     board.append([-1]+input_list+[-1])

# limit_line = [[-1 for i in range(m+2)]]
# board = limit_line + board + limit_line

#######1차 구현 풀이 failed..#####
import copy

######### functions
def search_area(dot, board):
    global power

    queue = []
    board[dot[0]][dot[1]] = 0

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for el in d:
        x = dot[0] + el[0]
        y = dot[1] + el[1]

        for i in range(power[dot]):
            if board[x][y] == -1:
                break
            elif board[x][y] != 0:
                queue.append((x, y))
            x += el[0]
            y += el[1]

        return [queue, board]


def get_left(board):
    cnt = 0
    new_queue = []
    for i in range(1, len(board)-1):
        for j in range(1, len(board)-1):
            if board[i][j] != 0 and board[i][j] != -1:
                new_queue.append((i, j))
                cnt += 1
    return [cnt, new_queue]


def BFS(root, board):
    copy_board = copy.deepcopy(board)
    queue = [root]

    while len(queue) != 0:
        top = queue.pop(0)
        if copy_board[top[0]][top[1]] == 0:
            continue
        [next_queue, next_copy_board] = search_area(top, copy_board)
        queue += next_queue
        copy_board = next_copy_board

    [left, new_queue] = get_left(copy_board)

    if left == 0:
        return 0
    else:
        return {
            'left': left,
            'board': copy_board,
            'queue': new_queue
        }


def get_result(board, queue):
    min_left = 20

    for dot in queue:
        result = BFS(dot, board)

        if result == 0:
            return 0
        else:
            if result['left'] < min_left:
                min_left = result['left']
                min_board = result['board']
                min_queue = result['queue']

    return [min_board, min_queue]
    
##### functions


t = int(input())
for case in range(1,t+1):
  n, m, k = map(int, input().split())
  
  board = []
  power = {}
  queue = []
  
  for i in range(n):
      input_list = list(map(int, input().split()))
      for j, val in enumerate(input_list):
          if val != 0:
              queue.append((i+1, j+1))
              power[(i+1, j+1)] = val
      board.append([-1]+input_list+[-1])
  
  limit_line = [[-1 for i in range(m+2)]]
  board = limit_line + board + limit_line
  
  answer = 0 
  
  while True:
    result = get_result(board, queue)
    k -= 1 
    if k < 0:
      answer += 1

    if isinstance(result,int):
      if k >= 0:
          print("#%s %s" % (case, 0))
          break
      else:
          print("#%s %s" % (case, answer))
          break
    else:
          board = result[0]
          queue = result[1]
  
######1 차 구현풀이 (failed) #######

# 문제점 :
# - 잔실수였음 전부다..
# - return문을 for문바깥에 해야하는데 안쪽에 해두는 실수
# - 배열 탐색 범위를 초과하여 탐색해서 나오는 runtime error 
# - 로직 및 설계는 맞았다!

# 코멘트 : 차분하게 하나하나 설계하면 분명히 풀 수 있었다


##### 2차 구현 풀이(success)!!! ######

import copy

######### functions
def search_area(dot, board):
    global power
    
    queue = []
    board[dot[0]][dot[1]] = 0

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for el in d:
        x = dot[0] + el[0]
        y = dot[1] + el[1]
        
        for i in range(power[dot]):
            if board[x][y] == -1:
                break
            elif board[x][y] != 0:
                queue.append((x, y))
            x += el[0]
            y += el[1]

    return [queue, board]


def get_left(board):
    global n 
    global m 
    
    cnt = 0
    new_queue = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] != 0 and board[i][j] != -1:
                new_queue.append((i, j))
                cnt += 1
    return [cnt, new_queue]


def BFS(root, board):
    copy_board = copy.deepcopy(board)
    queue = [root]

    while len(queue) != 0:
        top = queue.pop(0)
        if copy_board[top[0]][top[1]] == 0:
            continue
        [next_queue, next_copy_board] = search_area(top, copy_board)
        queue += next_queue
        copy_board = next_copy_board
  
    [left, new_queue] = get_left(copy_board)

    if left == 0:
        return 0
    else:
        return {
            'left': left,
            'board': copy_board,
            'queue': new_queue
        }


def get_result(board, queue):
    min_left = 100
    min_board = []
    min_queue = []
    
    for dot in queue:
        result = BFS(dot, board)
        if result == 0:
            return 0
        else:
            if result['left'] < min_left:
                min_left = result['left']
                min_board = result['board']
                min_queue = result['queue']
                
    if len(min_board) == 0 or len(min_queue) == 0:
      return 0
    else:
      return [min_board, min_queue]

t = int(input())
for case in range(1,t+1):
  n, m, k = map(int, input().split())
  
  board = []
  power = {}
  queue = []
  
  for i in range(n):
      input_list = list(map(int, input().split()))
      for j, val in enumerate(input_list):
          if val != 0:
              queue.append((i+1, j+1))
              power[(i+1, j+1)] = val
      board.append([-1]+input_list+[-1])
  
  limit_line = [[-1 for i in range(m+2)]]
  board = limit_line + board + limit_line
  answer = 0 
  
  while True:
    result = get_result(board, queue)
    k -= 1 
    
    if k < 0:
      answer += 1

    if isinstance(result,int):
      if k >= 0:
          print("#%s %s" % (case, 0))
          break
      else:
          print("#%s %s" % (case, answer))
          break
    else:
          board = result[0]
          queue = result[1]
  