result = 0
answer = 0
results = ""
arr = set([])
cnt = 0
def solution(numbers, target):
    
    def recursion(idx=0) :
        global result
        global answer 
        global results 
        global arr 
        global cnt 
        
        cnt+=1 
        if len(numbers[idx:]) == 0:
            if result == target and results not in arr:
                arr.add(results)
                answer += 1 
            return 
        else:
            el = numbers[idx]
            
            result += el * -1
            results += str(el * -1)
            recursion(idx+1)
            result -= el * -1
            results = results[:-len(str(el * -1))]
            
            result += el
            results += str(el)
            recursion(idx+1)
            result -= el
            results = results[:-len(str(el))]
    
    recursion()
    return answer