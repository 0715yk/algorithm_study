result = 0
max_result = 0

def recursion(arr) :
    global result
    global max_result
    
    if 0 == len(arr):
        if result > max_result:
            max_result = result
        return 

    for idx,el in enumerate(arr):
        result+= el 
        if idx-1 < 0 :
            idx_prev = (abs(idx-1) % len(arr)) * -1
        else:
            idx_prev = (idx-1) % len(arr)
        copy_arr = arr[:]
        idx_next = (idx+1) % len(arr)
        print(idx_prev, idx_next)
        if idx_prev < 0:
            print(arr[idx_next+1:idx_prev])
            recursion(arr[idx_next+1:idx_prev])
        else:
            print(arr[idx_next+1:idx_prev])
            recursion(arr[idx_next+1:idx_prev])
        result -= el
            
def solution(sticker):
    global max_result
    
    recursion(sticker)
    
    return max_result


    # 재귀함수
    # 배열을 매개변수로 넣으면서
    # 그 배열을 바탕으로 for 문을 돌리는데
    # 이전에 담은 수를 계속 어딘가에 넣으면서 재귀를 돌려야함
    # 더이상 돌릴 수 없는 것이 기저조건으로 매개변수 배열이 비면 리턴
    
    # 하나를 선택했으면 그 양옆의 요소를 지운 배열을 재귀로 돌림
    # 그럼 똑같이 또 하나를 선택 해서 똑같은 재귀 반복
    # 하다가 끝까지 갔을 떄 즉, 하나의 요소도 남지 않았을 때(왜나면 자연수 모음이기때문에 무조건
    # 더할 ㅅ ㅜ 있는건 싹다 더해야 최대임
    



    # 만약에 7+1 = 8이면 배열의 인덱스를 넘어가는데 이걸 다시 0으로 바꾸려면
     # 인덱스 % 8 로하면되지 않을까
        # 1% 8 =1 0 % 8 = 0 => 9 %8 1 
    # abs(-9) % 8= 01 
    # -는 abs한다음 8로 나눈 나머지에 - 해주면 됨
    
    # 14, = (5,11,3,9,2) => 
    # 5=> 3,9,2,
    # for문을 통해 처음부터 끝까지 탐색하는데 그 숫자를 기준으로
    # 양옆을 없애고, 남은 수를 가지고 또 .. 이건 재귀로 해야할듯
    
    
    
    # 그 다음에 해당 배열에서 인덱스 조합을 통해 
    # 3개를 뽑는데, 이 때 주의할 것이 하나를 뽑으면 그 인덱스 -1,+1은 버려야함
    # 그렇게 3개를 뽑아서 최대값이 되는 경우의 수에서의 합을 리턴하는 것이 문제

    # 실패..
    # 인터넷 검색 후 DP 문제라는데 다시 풀어봐야겠다..
    