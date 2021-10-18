# 처음 풀이 1 
# 평소 소수를 판별하는 방법을 쓰면 시간복잡도에서 걸릴 것 같아서 
# 처음에는 '에라토스테네스의 체' 원리를 이용해서 풀고자 했다.
# ** 처음에 문제를 제대로 파악하지 못하고 중복을 제거해서 문제가 됐었다 - (오답부분)

from itertools import combinations

def solution(nums): 
    global cnt
    answer = 0
    total_arr = []
    for i in combinations(nums, 3):
        total_arr.append(sum(list(i)))
    # combinations 모듈을 써서 nums 요소 3개로 만들 수 있는 모든 조합을 만든다.
    total_arr.sort() # nlogN
    copy_total = [i for i in range(2,total_arr[-1]+1)]
    # 에라토스테네스의 체를 쓰기 위해 2부터 total_arr의 가장 큰 값까지 배열을 만든다.

    for i in range(len(copy_total)-1):
        if copy_total[i] == False:
            continue
        for j in range(i+1, len(copy_total)):
            if copy_total[j] == False:
                continue
            if copy_total[j] % copy_total[i] == 0:
                copy_total[j] = False
    # 에라토스테네스의 체를 사용하여 2부터 total_arr의 가장큰수까지 모든 수를 바탕으로 소수를 걸러낸다.
    copy_total = list(set(copy_total)) # 소수만 남은 배열
    for el in total_arr:
        if el in copy_total:
            answer += 1
    return answer

# 생각해보니 이정도면 일반 소수 체크 로직을 써도 괜찮겠다 싶어 만든 두번째 풀이
# 코드는 훨씬 간결함
# 속도도 이게 훨씬 빠름... 너무 어렵게 생각했다..

import math
from itertools import combinations

def check_prime(num):
    global cnt
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums): 
    answer = 0
    total_arr = []
    for i in combinations(nums, 3):
        total_arr.append(sum(list(i)))
    for el in total_arr:
        if check_prime(el):
            answer += 1
    return answer


# 처음 문제를 풀 때 썼던 수도코드 

# 세미 에라토스테네스의 체?
# 일단 3자리수로 만들 수 있는 모든 수를 배열에 담는다
# 그다음 그걸 정렬한다
# 그러면 일단 가장 작은 수가 있을 것
# 그 수가 소수인지 판별해서 소수면 그 수의 배수는 다 지우기
# 소수가 아니어도 그수와 관련된 배수는 다지워도됨 ㅇㅇ
# 그렇게 똑같은 시행을 반복하다보면 다 지워지고 남는 수들이 있을건데
# 그게 소수지 않을까?
# 근데 이건좀 말이안되는듯..
# 예를 들어, 234,235,236 이렇게 연속으로 있으면...
# 그것보다 그러면 
# 제일 작은 수보다 작은수들로 채우고
# 그냥 2부터 시작해서 지우고
# 3부터 시작해서 지우고
# 4ㅡ5 => 쭉간다음에 그 뒤부터는 있는 수들로 지우기 
# 아니면 2부터 가장 큰수까지 소수 에라토스테네스의 체로 구한다음에
# 전체 소수 배열이랑 3개씩 더해서 걸러낸 배열이랑 교집합 구하면 그게 정답?<-이거네

# 에라토스테네스의 체로 2부터 3개의 수를 더했을 때의 수들의 집합중 가장 큰수까지 모든 자연수에
# 소수 걸러냄
# 그러면 배열이 하나나올거고
# a라고 해보자 그배열을
# a와 3개씩 더해서 구한 모든 수의 배열(b)의 교집합에 소수가 담겨있을 것
# 1) 에라토스테네스의 체로 1~ 최대값까지 소수를 담은 배열
# 2) 모든 수의 배열과 소수를 담은 배열간의 교집합 찾기
# 그러면 그 수의 배수는 다지우기