## template
cases = int(input())

for case in range(1,cases+1):
  n,m,cnt = map(int, input().split())
  ap_arr = []
  
  for i in range(cnt):
    ap_arr.append(list(map(int,input().split())))
  
  steps_cnt = int(input())
  a_steps = list(map(int,input().split())) + [0]
  b_steps = list(map(int,input().split())) + [0]
  
  a_location = list(map(int,input().split()))
  b_location = list(map(int,input().split()))
  
  dx = [0,-1,0,1,0]
  dy = [0,0,1,0,-1]
  
  for step in range(steps_cnt+1):
    # 이게 a,b가 이동한 좌표값  
      
    a_ap = set([])
    b_ap = set([])
    
    for ap in ap_arr:
      if abs(a_location[1]-ap[1]) + abs(a_location[0]-ap[0]) <= ap[2]:
        a_ap.add(ap[3])
      if abs(b_location[1]-ap[1]) + abs(b_location[0]-ap[0]) <= ap[2]:
        b_ap.add(ap[3])
    if len(a_ap) == 0 and len(b_ap) == 0:
      pass
    elif len(a_ap) == 0:
      b_location[2] -= max(list(b_ap))
    elif len(b_ap) == 0:
      a_location[2] -= max(list(a_ap))
    else:
      # 둘다 1개 이상의 공유기 안에 있을 때
      # 그렇다고 하더라도 max값만 안같으면 상관없음
      if max(list(b_ap)) != max(list(a_ap)):
        b_location[2] -= max(list(b_ap))
        a_location[2] -= max(list(a_ap))
      else:
        # max 값이 같으면 max값의 1/2 을 한값과
        # 각각 1순위 2순위를 더한값을 비교
        b_ap = list(b_ap)
        b_ap.sort()
        a_ap = list(a_ap)
        a_ap.sort()
        
        if len(b_ap) >= 2 and len(a_ap) >=2 :
          first = a_ap[-1] + b_ap[-2]
          second = a_ap[-2] + b_ap[-1]
          if  first > second:
            b_location[2] -= b_ap[-2]
            a_location[2] -= a_ap[-1]
          elif first < second:
            b_location[2] -= b_ap[-1]
            a_location[2] -= a_ap[-2]
          else:
            if a_location[2] > b_location[2]:
              b_location[2] -= b_ap[-2]
              a_location[2] -= a_ap[-1]
            elif a_location[2] < b_location[2]:
              b_location[2] -= b_ap[-1]
              a_location[2] -= a_ap[-2]
            else:
              b_location[2] -= b_ap[-2]
              a_location[2] -= a_ap[-1]
        elif len(b_ap) >= 2 and len(a_ap) == 1:
          b_location[2] -= b_ap[-2]
          a_location[2] -= a_ap[-1]
        elif len(a_ap) >= 2 and len(b_ap) == 1:
          b_location[2] -= b_ap[-1]
          a_location[2] -= a_ap[-2]
        else:
          b_location[2] -= b_ap[-1]//2
          a_location[2] -= a_ap[-1]//2
    
    a_location[0]+=dx[a_steps[step]]
    a_location[1]+=dy[a_steps[step]]
    
    b_location[0]+=dx[b_steps[step]]
    b_location[1]+=dy[b_steps[step]]
    
  if a_location[2] < 0:
    a_location[2] = 0
  if b_location[2] < 0:
    b_location[2] = 0
    
  print("#%s %s %s" % (case, a_location[2],b_location[2]))