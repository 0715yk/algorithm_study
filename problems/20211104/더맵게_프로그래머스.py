import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 전부다 K이상으로 만드는 것이 목표(scoville 배열에 있는 지수를)
    # 가장 작은 것을 꺼냈을 때 K미만이면 두번째것도 꺼내서 섞어야함
    # 이렇게 계속 작은 것을 꺼냈을 때 K이상일 때까지 해야함
    # 최소힙을 이용하면 될듯?
    # 근데 -1이 나오는 경우는 그러면.. recursion limit을 넘어가는 케이스?
    try:
        while True:
            first = heapq.heappop(scoville)
            if first >= K:
                break
            else:
                answer += 1 
                second = heapq.heappop(scoville)
                heapq.heappush(scoville, first + (second*2))
    except:
        return -1
    
    return answer