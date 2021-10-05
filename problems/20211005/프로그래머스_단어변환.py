def solution(begin, target, words):
    answer = 0
    # BFS !
    queue = [begin]
    path = {}
    path[begin] = True
    
    def is_possible(word1,word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1 
        if cnt == len(word1) - 1 :
            return True
        else:
            return False
        
    flag = False
    
    while len(queue) != 0:
        answer += 1 
        top = queue.pop()
        for word in words:
            try:
                if path[word]:
                    continue
            except:
                if is_possible(top, word):
                    if word == target:
                        flag = True
                        break
                    path[word] = True 
                    queue.append(word)
                else:
                    continue
        if flag:
            return answer
            
    return 0