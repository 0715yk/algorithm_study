def search_protein(dot):
    global maps

    ways = [(-1,0), (0,1), (1,0), (0,-1)]
    visit ={}
    result = maps[dot[0]][dot[1]]
    visit[result] = True
    for way in ways:
        x = dot[0] + way[0]
        y = dot[1] + way[1]

        while maps[x][y] != -1:
            try:
                if visit[maps[x][y]]:
                  x += way[0]
                  y += way[1]  
            except:
                visit[maps[x][y]] = True
                result += maps[x][y]
                x += way[0]
                y += way[1]        

    return result

t = int(input())

for case in range(1,t+1):
  n = int(input())
  
  limit_line = [[-1 for i in range(n+2)]]
  maps = []
  
  for i in range(n):
      maps.append([-1]+list(map(int, input().split()))+[-1])
  
  maps = limit_line + maps + limit_line
  answer = 1
  
  for i in range(2,n):
      for j in range(2,n):
          protein = search_protein((i,j))
          if protein > answer:
              answer = protein
              
  print("#%s %s" % (case, answer))


  ## 한번에 클리어!