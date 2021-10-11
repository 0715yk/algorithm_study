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

# 매번 sorted를 하는게 문제인 것 같아서 sorted를 빼봤음
# sorted를 빼도 해결이 안돼서 생각해보니 굳이 BFS를 안해도 될 것 같음
# 그 주변만 도는 구현법을 알고 있으니까 그렇게 접근해보자 .
# def get_max(root):
#   global maps
#   global k 
#   global n
#   global m

#   meter = []
#   # root dot을 가지고 한칸씩 위로 가면서 그 다이아몬드 모양으로 주변을 돌면서
#   # 똑같이 meter값을 구하면 될듯 inform 필요없음(path도 그렇고)

#   idx = 1
#   now = (root[0]-idx,root[1])
#   dx = [1,1,]-
#   dy = [1,-1,]
#   while maps[now[0]][now[1]] != -1 :
#     for j in range(4):
#       for i in range(idx):
#         now[0]-=1 
#         now[1]+=1 
#         board[now[0]][now[1]] = idx 

  
#   for i in range(1, len(meter)+1):
#       num = i
#       sum_num = 0
#       sum_peo = 0
#       for val in meter[:i]:
#           sum_num += val * num 
#           sum_peo += val 
#           num -= 1
#       if sum_num > result:
#           if sum_num <= k:  
#               result = sum_num
#               answer = sum_peo
#           else:
#               return answer                    
  
#   return answer


# t = int(input())

# for case in range(1,t+1):

#   n,m,k = map(int, input().split())
#   maps = []
  
#   for i in range(n):
#       maps.append([-1]+list(map(int, input().split()))+[-1])
  
#   limit_line = [[-1 for i in range(m+2)]]
#   maps = limit_line + maps + limit_line
  
#   answer = 0
#   for i in range(1,n+1):
#     for j in range(1,m+1):
#         dot = (i,j)
#         result = get_max(dot)
#         if result > answer:
#           answer = result
  
#   print("#%s %s" % (case, answer))
  



