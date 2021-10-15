cases = int(input())

for case in range(1,cases+1):
  n,m = map(int, input().split())
  board = []
  
  d = {}
  left = n*m
  answer = {}
  
  for i in range(n):
    input_list = list(input())
    for j,el in enumerate(input_list):
      if el == '0':
        continue
      else:
        try:
          d[el].append([(i+1,j+1),0,el])
        except:
          d[el] = [[(i+1,j+1),0,el]] 
      input_list[j] = "0"
    board.append([-1]+input_list+[-1])
    
  limit_line = [[-1 for i in range(m+2)]]
  board = limit_line + board + limit_line
  l = []
  for key in sorted(d,reverse=True):
    l+=d[key] 
  
  height = {}
  
  for i in range(1,11):
    height[chr(64+i)] = i 
  # [(1, 3), 0, 'C']
  
  while left != 0:
    l[0][1] += 1 
    # 매 시행마다 키를 +1 해줌 
    top = l.pop(0)
    indx = top[0]

    if top[1] == 1:
      if board[indx[0]][indx[1]] == '0':
        try:
          answer[top[2]] += 1 
          left -= 1
          board[indx[0]][indx[1]] = top[2]
        except:
          answer[top[2]] = 1
          left -= 1
          board[indx[0]][indx[1]] = top[2]
      else:
        continue
    # 만약에 +1 했는데 최대키면? 
    # 상하좌우에 포자를 뿌림
    if height[top[2]] == top[1]:
      for way in [(indx[0]-1,indx[1]),(indx[0],indx[1]+1),(indx[0]+1,indx[1]),(indx[0],indx[1]-1)] :
        if board[way[0]][way[1]] == -1 or board[way[0]][way[1]] != "0":
          continue
        l.append([way,0,top[2]])
    else:
      # 최대키가 아니면
      # 그대로 키만 +1 한채로 다음으로
      l.append(top)
      continue
  result = ""
  for key in list(height.keys()):
    try:
      result += " " + str(answer[key])
    except:
      result += " 0"
  print("#%s%s" % (case, result))
        
        
        