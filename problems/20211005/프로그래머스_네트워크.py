def solution(n, computers):
    graph = {}
    path = {}
    answer = 0
    
    for i in range(n):
        graph[i] = []
        for idx, el in enumerate(computers[i]):
            if el == 1 and i!=idx:
                graph[i].append(idx)

                    
    def dfs(node):
        for el in graph[node]:
            try:
                if path[el]:
                    continue
            except:
                path[el] = True
                dfs(el)

    
    for key in list(graph.keys()):
        try:
            if path[key]:
                continue
        except:
            answer += 1 
            dfs(key)
            
    return answer