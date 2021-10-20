def solution(s, n):
    answer = ''
    # s를 각각 다 나눠서
    l = list(s)
    # 그 리스트에 대해서
    # chr() + n으로 만들고 다시합치기
    abc = [chr(i) for i in range(97,123)]
    ABC = [chr(i) for i in range(ord("A"),ord("Z")+1)]
    abc_l = len(abc)

    for idx, el in enumerate(l):
        if ord(el) == 32:
            answer+= " "
        elif ord(el) >= 97 and ord(el) <= 122:
            answer += abc[(abc.index(el) + n) % abc_l]
        else:
            answer += ABC[(ABC.index(el) + n) % abc_l]
    
    return answer