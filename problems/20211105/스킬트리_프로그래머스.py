def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        word = ""
        for i in range(len(tree)):
            if tree[i] in skill:
                word+=tree[i]
        if len(word) == 0:
            answer += 1 
            continue
        # 여기까지 skill 과 관련된것만 추렸음
        # 그럼 여기서부터 관련된 것들이 순서에 맞는지만 보면됨.
        # 일단 시작은 무조건 skill[0]으로해야함 그렇지 않으면 빌드가 불가능
        # [0]으로 시작하고 and 뒷부분이 같으면 통과임
        # 근데 0 이외의 것으로 시작하면 전부다 fail
        # 일단 그러면 시작값을보자
        if word[0] != skill[0]:
            continue
        else:
            # 일단 시작값은 맞음
            # 뒷부분 순서도 같아야함
            if word in skill:
                answer += 1
            else:
                continue
    return answer