def solution(arr1, arr2):
    answer = []
    #[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
    # 0 0 
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer