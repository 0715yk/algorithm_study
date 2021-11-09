# 문제 : 124 나라의 숫자(프로그래머스 level 2)
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12899

# 1) 1차 풀이(실패..)
from itertools import product
import math

def solution(n):
    answer = ''
    idx = math.ceil(math.log((n*2)+3,3)-1)
    num = ((3**(idx+1)) - 3) / 2
    num -= 3 ** idx
    cnt = int(n - num)

    results = []
    nums = ['1','2','4']
    for idx, num in enumerate(product([0,1,2], repeat=idx)):
        if idx+1 == cnt:
            for el in list(num):
                answer += nums[el]
            break

    return answer

    # 1,2,4
    # 완전탐색으로 했을 때
    # [1,2,4]
    # 0,1,2, 
    # 00, 01, 02, 10, 11, 12, 20, 21, 22, 
    # 000, 001, 002, 010, 011, 012, 020, 021, 022 ...이런식으로 쭉가는데
    # 이렇게 쭉한다 했을 때 문제를 풀 수 없는게 n이 5억임
    
    # 그러면 다른 방법을 찾아야함.
    # 규칙을 찾아보니까
    # 3-3^x 3-3^(x+1) 까지의 합에 n이 속하면 
    # 3부터 3^x까지의 합을 구하다가 n이 해당 숫자보다 작거나 같으면 n은
    # 124나라의 숫자 x개로 이뤄진 십진수라는 것을 알 수 있다
        # 이제 124나라의 숫자 idx개로 이뤄진 십진수 n이 실제 124 나라에서 몇인지 구해야한다
    # 그래도 케이스를 많이 줄인 것인게 124나라의 숫자 idx개로 만들 수 있는 케이스만 고려하면됨.#
    #
    
    # 여기서부터 idx개로 이뤄진 124나라의 숫자를 완전탐색하되, cnt번만 탐색하고 멈춘다.r

# 시간 초과로 실패..


# 2) 2차 풀이

def solution(n):
    answer = ""
    l = ['4','1','2']
    while n > 0:
        q = n // 3
        r = n % 3 
        answer = l[r] + answer
        n //= 3 
        if r == 0:
            n -= 1
    
    return answer


# 코멘트 : 규칙을 찾아내는 것이 포인트인 문제.. 반드시 다시 풀어보기. 너무 머리써서 풀려고 하지말고, 차근차근 규칙을 찾아보려는 자세를 갖자 이런 유형은