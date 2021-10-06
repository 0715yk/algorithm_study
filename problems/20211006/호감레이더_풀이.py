def get_max(root):
  global maps
  global k 
  
  queue = [root]
  path = {}
  inform = {}
  inform[root] = 0
  meter = {}
  
  while len(queue) != 0 :
      top = queue.pop(0)
      path[top] = True
  
      for way in [(top[0]-1,top[1]), (top[0],top[1]+1), (top[0]+1,top[1]), (top[0],top[1]-1)]:
          try:
              if path[way]:
                  continue
          except:
              if maps[way[0]][way[1]] == -1:
                path[way] = True
                continue
              queue.append(way)
              if maps[way[0]][way[1]] == 1:
                  inform[way] = inform[top] + 10 
                  try:
                      meter[inform[top] + 10]+= 1 
                  except:
                      meter[inform[top] + 10] = 1 
              else:
                  inform[way] = inform[top] + 10 
                  try:
                    if meter[inform[top] + 10]:
                      continue
                  except:
                    meter[inform[top] + 10] = 0 
              path[way] = True
  
  result = -1 
  answer = 0
  
  for i in range(1, len(list(meter.keys()))+1):
      num = i
      sum_num = 0
      sum_peo = 0
      for key, val in sorted(meter.items())[:i]:
          sum_num += val * num 
          sum_peo += val 
          num -= 1
      if sum_num > result:
          if sum_num <= k:  
              result = sum_num
              answer = sum_peo
          else:
              return answer                    
  
  return answer


t = int(input())

for case in range(1,t+1):

  n,m,k = map(int, input().split())
  maps = []
  
  for i in range(n):
      maps.append([-1]+list(map(int, input().split()))+[-1])
  
  limit_line = [[-1 for i in range(m+2)]]
  maps = limit_line + maps + limit_line
  
  answer = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
        dot = (i,j)
        result = get_max(dot)
        if result > answer:
          answer = result
  
  print("#%s %s" % (case, answer))
  

# 1차 구현 결과 = 시간초과..