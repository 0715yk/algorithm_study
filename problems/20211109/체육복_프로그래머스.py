# 문제 이름 : 체육복 (프로글머스 level 1 그리디 유형)
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    # 원래는 n - len(lost) 만큼 수업을 들을 수 있음
    # 근데 여벌을 가져온 학생들이 있어서 len(lost)를 최대한 줄여보려고 하는 것
    # + 여벌 체육복을 가져온 사람의 번호가 lost에 있을 수 있다(즉, 여벌을 가져온 사람이 도난 당할 수 있음)
    origin = []
    
    for i in reserve:
        if i in lost:
            lost.remove(i)
        else:
            origin.append(i)
            
    origin_lost = lost[:]
    
    for i in origin :
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    first = len(lost)
    
    for i in origin :
        if i+1 in origin_lost:
            origin_lost.remove(i+1)
        elif i-1 in origin_lost:
            origin_lost.remove(i-1)
            
    second = len(origin_lost)
    
    lost = second if first>second else first
    
    answer = n - lost
    
    return answer