# def solution(s):
#     # 인덱스 1부터 문자열의 길이 -2 인덱스까지 탐색
#     # 탐색하면서 각각 인덱스에 해당하는 문자열의 양옆으로 한칸씩 이동하면서 펠린드롬인지 측정
#     # 만약에 펠린드롬이 아니면 break 하고 다음으로
#     # 만약에 펠린드롬이 맞으면 계속해서 카운트 해나감 이 때 cnt =1 로 시작이고
#     # 한번씩 양옆으로 +1 될 때마다 +2해주면 됨(전체 펠린드롬 길이이므로)
#     # 이 때, 양옆으로 가는 인덱스가 0과 길이-1을 초과 미만이 된다면 break임 
#     # break할 때도 펠린드롬을 확인하겠지 ㅇㅇ
    
#     if len(s) == 2:
#         if s[0] == s[1]:
#             return 2
#         else:
#             return 1
    
#     l = list(s)
#     max_cnt = 1
#     for idx, a in enumerate(l):
#         if idx == 0 or idx == len(l)-1:
#             continue
#         else:
#             cnt = 1
#             step = 1
#             while True:
#                 if idx-step < 0 or idx+step>len(l)-1:
#                     break
#                 if l[idx-step] == l[idx+step]:
#                     cnt+=2 
#                     step += 1 
#                 else:
#                     break
                    
#             if max_cnt < cnt:
#                 max_cnt = cnt
#     return max_cnt

# 위의 풀이대로하면 짝수를 못걸러낸다..즉 4나 6길이를 못걸러냄
# 펠린드롬을 중간을 기준으로 양옆이 같은거라고 착각함
# 펠린드롬은 뒤집었을 때 같은 값을 갖는 것이다.
def solution(s):
    # 다시 풀어보면
    # 인덱스 1부터 시작해서 앞으로 2개 3개 4개.. 씩 되는데까지 하나하나 계산해보면 됨
    # 인덱스 1에서는 앞의 인덱스 0과 함께의 경우밖에 없음
    # ab != ba 
    # 인덱스 2로 가면 ba != ab 이게 인덱스1과의 조합이고
    # 인덱스 0까지의 조합을하면 aba == aba로 체크 
    # 이런식으로하면 앞에 부분은 앞에서 하고 뒤로 가도 겹치는걸 계산안한다
    
    l = list(s)
    answer = 1
    
    for idx in range(len(l)-1,0,-1):
        if idx+1 <= answer:
            break
        for j in range(0,idx):
            words = l[j:idx+1]
            num = len(words)
            if answer >= num:
                break
            if "".join(words) == "".join(reversed(words)):
                answer = num
                break
    return answer
                
# 시간 초과!(정확성은 통과함)
# 효율성 테스트 1이 자꾸 걸림

# 아래와 같이 reversed가 문제인 것 같아서 reversed를 한번만 쓰는 방향으로 다시 만들어봤으나
# 이것도 통하지 않음..ㅎ
def solution(s):
    l = list(s)
    answer = 1
    
    for idx in range(len(l)-1,0,-1):
        if idx+1 <= answer:
            break
        reverse_l = "".join(reversed(l[:idx+1]))
        for j in range(0,idx):
            num = len(reverse_l)
            words = l[j:idx+1]
            if answer >= num:
                break
            if "".join(words) == reverse_l:
                answer = num
                break
            reverse_l = reverse_l[:-1]
    return answer

# 애초에 다른 알고리즘을 써야하는듯
# 지금 문제는 이중 for문으로 뒤에서부터 거의 완전탐색식으로 검색을 하고 있다는 것임.
# 그러면 이걸 이중 for문으로 안하려면 ..?
# 분할해서 푸는법밖에는 일단은 안떠오름

# 최종 해결 
def solution(s):
    answer = 1
    for idx in range(len(s)-1,0,-1):
        if idx+1 <= answer:
            break
        for j in range(0,idx):
            num = len(s[j:idx+1])
            if answer >= num:
                break
            if s[j:idx+1] == s[j:idx+1][::-1]:
                answer = num
                break
    return answer
