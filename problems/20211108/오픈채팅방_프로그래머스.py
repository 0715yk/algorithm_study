# 레벨 : level 2 (2019 kakao blind 기출)
# 문제 이름 : 오픈채팅방
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    # answer에는 들어왔습니다, 나갔습니다 의 기록만 쓰여짐
    # record에서 들어왔습니다, 나갔습니다 정보가 들어있는데,
    # 아이디 - 닉네임 
    # record에 들어왔습니다, 나갔습니다는 스택처럼 쌓이고
    # change를 통해 그 스택처럼 쌓인 정보의 닉네임만 계속 바뀜
    # 최종적으로 보게되는 스택을 리턴해야되니까 결론적으로 change 정보를 가지고
    # 각 아이디의 마지막 닉네임을 추적하고,
    # record의 들어왔습니다, 나갔습니다의 아이디를 통해 마지막 닉네임을 템플릿처럼 껴넣고 리턴 배열에 넣으면 됨
    
    # 근데 일단 배열 길이가 100,000이다 최대
    # 먼저, 이중에 change만 걸러내서 for문을 돌리자(100,000+100,000)
    # 그러면 최종적으로 딕셔너리에 아이디별 닉네임을 얻을 수 있음(최종)
    # 그리고 다시 change가 없는 record배열에서 아이디 별로 최종 닉네임을 바탕으로 리턴 배열을 만든다(100,000)
    # 최대 30만 정도로 시간복잡도 통과가능
    
    # 위의 방법에서 틀린 것이 나갔다가 들어올 때 닉네임을 바꾸는 것을 체크할 수 없음
    # 따라서 record를 전체 탐색하면서 최종 닉네임을 얻어내는 방식으로 가야한다. 
    
    change = []
    pure_record = []
    nickname = {}
    
    for el in record:
        el_l = el.split(' ')
        if el_l[0] == "Change":
            nickname[el_l[1]] = el_l[2]
        else:
            try:
                nickname[el_l[1]] = el_l[2]
            except:
                pass
            pure_record.append(el)
    
    for record in pure_record:
        el_l = record.split(' ')
        if el_l[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % nickname[el_l[1]])
        else:
            answer.append("%s님이 나갔습니다." % nickname[el_l[1]])
            
    return answer