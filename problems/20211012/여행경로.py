answer=  ["ICN"]

def recursion(node,d,l):
    global answer
    
    if l == 0:
        return True
    try:
        if d[node]:
            pass
    except:
        return
    
    for idx, airport in enumerate(d[node]):
        answer.append(airport)
        top = d[node].pop(idx)
        
        if recursion(top,d,l-1):
            return True

        d[node].insert(idx,top)
        answer.pop()


    
def solution(tickets):
    d = {}
    
    for el in tickets:
        try:
            d[el[0]].append(el[1])
        except:
            d[el[0]] = [el[1]]
            
    for key, val in d.items():
        val.sort()
        d[key] = val
        
    l = len(tickets)
    root = "ICN"
    recursion(root,d,l)
    
    return answer