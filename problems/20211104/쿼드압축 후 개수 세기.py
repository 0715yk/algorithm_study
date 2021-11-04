def solution(arr):
    answer = {1:0, 0:0}
    def check_all(arr):
        prev = arr[0][0]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != prev :
                    return -1
                else:
                    prev = arr[i][j]
                    continue 
        return prev
    
    def recursion(arr) :
        if len(arr) == 1:        
            answer[arr[0][0]] += 1 
            return 
        num = check_all(arr)
        if  num != -1:
            answer[num] += 1 
            return 
        else:
            # 4등분 해서 재귀함수
            first = []
            second = []
            third = []
            fourth = []
            
            for i in range(len(arr)//2):
                a= []
                b= []
                for j in range(len(arr)//2):
                    a.append(arr[i][j])
                for j in range(len(arr)//2,len(arr)):
                    b.append(arr[i][j])
                first.append(a)
                second.append(b)
            for i in range(len(arr)//2,len(arr)):
                c=[]
                d=[]
                for j in range(len(arr)//2):
                    c.append(arr[i][j])
                for j in range(len(arr)//2,len(arr)):
                    d.append(arr[i][j])
                third.append(c)
                fourth.append(d)
            recursion(first)
            recursion(second)
            recursion(third)
            recursion(fourth)
    recursion(arr)
    
    return [answer[0],answer[1]]

    # 재귀함수로 구현한다 했을 때
    # 기저 조건 : arr를 받아서 현재 받은 arr의 전체 중에 하나로 통일 돼 있으면 그 수를 +1해주고 return
    # 만약에 하나로 통일돼있지 않으면 => 4등분 한 다음에 각각의 배열을 재귀함수에 넣어줌 
    # 