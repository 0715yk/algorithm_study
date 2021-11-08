# level 2 (kakao 2020 blind 기출)
# 문제 이름 : 문자열 압축
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    results = []

    for i in range(1, (len(s) // 2)+1):
        cnt = 0
        answer = ""
        
        for j in range(0, len(s), i):
            if s[j:j+i] != s[j+i:j+i+i] :
                if cnt > 0:
                    answer += str(cnt + 1) + s[j:j+i]
                    cnt = 0
                else:
                    answer += s[j:j+i]
            else:
                cnt += 1

        results.append(answer)
        
    minimum = len(s)
    
    for el in results:
        if len(el) < minimum and len(el) != 0:
            minimum = len(el)
    
    return minimum


    # s를 받아서
    # 맨 앞부터 압축이 돼야하는 조건 (1)
    # aabbaccc
    # 1개 단위로 잘랐을 때 
    # a a = 2a
    # b b = 2b
    # a != c => a 
    # c = c = c => 3c
    # 2개 단위로 잘랐을 떄 
    # aa bb => x
    # 3개 단위로 잘랐을 때
    # aab bac => x
    # aabb accc => x
    # (length // 2) 단위까지 해보면 됨.
    # xababcdcdababcdcd 7개
    # 1 : x a  => x
    # 2 : ax ba => x
    # 3 : xab abc => x
    # 4 : xaba bcdc => x
    # 5 : xabab cdcda => x
    # 6 : xababc dcdaba => x
    # 7 : xababcd cdababc => x
    # abcabcabcabcdededededede
    # 11개
    # 1 : a b =>x 
    # 2 : ab ca => x
    # 3 : abc abc abc abc => 4abc // dededededede ded ede => x 
    # len // 2) -1 인덱스까지 탐색 
    
    # 1