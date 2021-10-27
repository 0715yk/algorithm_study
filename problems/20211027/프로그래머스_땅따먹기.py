def solution(land):
    answer = 0
    
    for row in range(1,len(land)) :
        for col in range(4):
            land[row][col] += max(land[row-1][:col] + land[row-1][col+1:])
    
    return max(land[len(land)-1])


    
    # 1) 탐색하면서 각행에서 최대값을 찾고, 그 최대값이 이전 값과 같으면
    # 그 다음 최대값을 선택하는 방식
    # => 그리디로 풀 수 없음. 
    
    # 2) 완전탐색으로 접근해야할듯
    # 는..4^100,000 임..
    
    # 3) DP 로 접근해보자
    # 1|2|3|5
    # 5|6|7|8
    # 4|3|2|1 
    # 1=>6=>2 9 
    # 1=>7=>4