cases = int(input())

patterns = { 
    1 : {
        0:2,
        1:0,
        2:3,
        3:1
    },
    2: {
        0:2,
        1:3,
        2:3,
        3:0
    },
    3: {
        0:1,
        1:3,
        2:0,
        3:2
    },
    4: {
        0:3,
        1:2,
        2:0,
        3:1
    },
    5: {
        0:2,
        1:3,
        2:0,
        3:1
    }
}

for case in range(1,cases+1):
  n = int(input())
  board = []
  warps = {}
  start_point = []
  max_cnt = -1
  
  for i in range(n):
    input_list = list(map(int, input().split()))
    
    for idx, el in enumerate(input_list):
      if el == 0:
        start_point.append((i+1,idx+1))
      if el >= 6 and el <= 10:
        try:
          prev = list(warps[el].keys())[0]
          warps[el][(i+1,idx+1)] = prev 
          warps[el][prev] = (i+1, idx+1)
        except:
          warps[el] = {}
          warps[el][(i+1, idx+1)] = None 
        
    board.append([5] + input_list + [5])
    
  limit_line = [[5 for i in range(n+2)]]
  board = limit_line + board + limit_line

  dx = [-1,0,1,-1]
  dy = [0,1,0,0]
  
  # 여기서부터 4방향으로 직진하는 while문을 만들어야함 
  for way in range(4):
    