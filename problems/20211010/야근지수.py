def solution(n, works):
    answer = 0
    # works 를 받으면 이 숫자들에서 n만큼을 선택해서 빼주고
    # 그 다음에 works의 모든 값들을 제곱해서 더해준 것이 야근 지수 인데
    # 이 야근 지수가 최소인 경우를 구하라는 것이 문제임
    
    # 탐색 공간을 먼저보면
    # 일단 포인트는 야근 피로도를 낮춰야하는 것이기에
    # 제곱을 하는 수 중에 가장 큰 수를 n으로 낮추는 것이 포인트일듯
    # 최대한 큰수들을 낮춰야 제곱한다음 더했을 때 그 수가 작아질 것
    # 그러므로 먼저 주어진 배열을 내림차순으로 정렬하고 (NlogN)
    # 같은 수끼리 묶자 (N)
    # 그렇게 묶은 다음에 하나하나 탐색하면서
    # 해당 배열의 개수가 4이고 남아있는 n이 8이면 
    # 가장 큰 수가 포함된 배열의 모든 수를 2씩 -1 하면 된다.
    # 만약에 개수가 4이고 n이 4보다 작은 3이면 
    # 1씩만 빼준ㄴ다
    # 만약 같으면 전부다 1씩 빼주고
    # 애매하게 6이나 10처럼 4보다큰데 딱 떨어지지않으면
    # 6%4 = 2  6//4 == 1 이니까 전부다 1씩빼주고 나머지 2개만 한번더 -1해준다
    # 이런식으로 해주면 되지 않을까?
    # 만약에 그러면 가장 큰수가 포함된 배열에 수가 1개가
    # 두번쨰 큰수가 포함된 배열의 수가 2개이고 n이 3개면?
    # 큰수가 포함된 배열에서 -1 해주고, 나머지 2개는 나머지 2개에서 쓰는 식
    # 근데 이게 시간복잡도가 되려나?
    # 먼저 정렬하는데 nLOGn, 정렬하고 같은 것끼리 묶을때 O(n)
    # 그것을 바탕으로 n을가지고 빼주면서 나아가는데에 최대 O(N)
    # 그렇게 O(N)씩 나아가면서 거기에 있는 수들을 제곱해주고 더해주는 것 까지 하면
    # 최대 O(K**2)
    
    # 이 방법보다 '최대값 죽이기'라는 관점에서보면
    # 계속해서 최대값을 찾아서 -1 해주고 n을 다 소진할 때까지 이 과정을 반복하면 확실히 답이다.
    # 근데 시간복잡도가 엉망이다 지금 상태로는
    # 예를 들어 max를 써서 최대값을 구하고,O(N)
    # 그 값을 찾고 index 그 찾은 값을 -1해주고 O(N)
    # 그 다음에 또 같은 시행을 반복하다가
    # n =0이되면 끝나고
    # 일단 n이 최대 백만이라.. n을 하나하나 빼주면서 하면 시간복잡도에서 무조건 걸림
    # 그 다음에 모든 수를 제곱해주면서 더해줘야함(O(N)
    # 일단 완전탐색법으로 풀면?
    while True:
        if n <= 0:
            break
        max_num = max(works)
        idx = works.index(max_num)
        if works[idx] == 0:
            break
        works[idx] -= 1 
        n-=1 
        
    for el in works:
        answer += el ** 2 
        
    return answer

    # 이렇게 풀면 정확성은 모두 통과지만 효율성이 위에서 말한대로 절대 불가능...

def solution(n, works):
    answer = 0
    # 그럼 여기서 좀더 효율적인 알고리즘을 찾아내야함
    # index, max 를 안써도 되는 알고리즘
    # 최초 한번만 nLOGn으로 sort하고,
    # 그 다음부터는 최대값을 하나씩 -1 하면서
    # 최대값이 변했나만 체크해주는식

    works.sort(reverse=True)
    
    while True:
        if n <= 0:
            break
        if works[0] == 0:
            break
        works[0] -= 1 
        n-=1 
        # 여기서 가장 큰 값이 맨앞에 오게 하기만하면됨
        # 이때 정렬 메서드를 안쓰고 최소의 시행으로 해야함
        std = works[0]
        for i in range(1,len(works)):
            if std >= works[i]:
                works[0],works[i-1] = works[i-1],works[0]
                break
            if i == len(works) - 1:
                if std < works[i]:
                    works.pop(0)
                    works.append(std)
                    break
                
    for el in works:
        answer += el ** 2 
        
    return answer

#     # 그래도 n이 너무커서 안되나보다..
#     # 아무래도..n을 1씩 쓰면 안될 것 같다.
#     # 처음 생각한 방법으로..
#     # {4:[4], 3:[3,3]}
#     # 이 있으면 혹은
#     # [[4],[3,3]] 이 있으면
#     # 이걸 맨 앞부터 [4]가 있으면
#     # 3이랑 맞추기 위해 n 을 배열의 길이만큼 -하고
#     # 그 다음 배열에 같은수를 길이만큼 추가한다
#     # 즉 첫번째 배열을 만났을 때 n을 -1 하고
#     # [[3,3,3]]으로 만드는것
#     # 그다음 배열을 봤더니 이제 없기에 이제는
#     # 여기다 n을 모두 쏟아붓고? 끝내면됨
    
# l = [[4],[2,2]]
# # 여기서
# n = 4 
# for idx, arr in enumerate(l):
#     try:
#         next_num = l[idx+1][0]
#         # 이거와 맞춰줘야함
#         now_num = l[idx][0]
#         num = now_num - next_num
#         # num = 2 
#         # num만큼 빼줘야함
#         maximum = n // num 
#         # 최대 4//2 = 2 2개만큼 2를 빼줄 수 있음
#         length= len(l[idx])
#         # 현재 탐색중인 배열의 길이가 1이므로
#         # 1개를 -1해주면 됨(즉, n을 1개쓰면됨)
#         # 다행히 1개있음 2개를 빼줄 수 있는데
#         if length > maximum:
            
#         elif length <= maximum:
#             del l[idx]
#             deleted = num * len(l[idx])
#             n -= deleted
#             l[idx+1].append([next_num] * deleted)

#     except:
#         # 만약에 없으면 처리를 해줘야함
#         print('hello')
import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    works = [-i for i in works]
    heapq.heapify(works) 
    for _ in range(n):
        w = heapq.heappop(works) + 1
        heapq.heappush(works, w)
    return sum([i**2 for i in works])


# 내가 고민하던 부분을 해결해주는것이 heap이었음
# 이렇게 하면 매회마다 O(N)혹은 O(NlogN)으로 재정렬 혹은 max값을 찾으면서 하지 않아도
# 2log(n) => heappop, heappush가 각각 logN 씩이니까
# 만의 시행으로 구할 수 있음. 즉 최악의 케이스에 n(백만) * 2logN임
# 결국 자료구조를 사용하는 문제였음!
