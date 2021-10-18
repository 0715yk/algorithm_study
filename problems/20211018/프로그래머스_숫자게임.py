# 정확히 이진탐색 문제는 아니고 파라메트릭 서치로 푸는 문제라고 생각하고 풀었던 문제
# 만약 찾은 숫자가 찾고자하는 숫자보다 크면
#   - 이전 숫자를 확인해서 찾고자하는 숫자 보다 작거나 같으면 찾은 숫자를 제거 후 +1
#   - 이전 숫자를 확인해서 찾고자하는 숫자 보다 크면 s~ 그숫자까지 재귀
# 만약 찾은 숫자가 찾고자하는 숫자보다 작으면
#   - 바로 다음 수를 봐서 찾고자하는 수보다 크면 +1 리턴
#   - 만약 찾고자하는 숫자보다 작거나 같으면 그수부터 e까지 재귀
# 만약 찾은 숫자가 찾고자하는 숫자와 같으면
#   - 그 다음수가 만약 크면
#   - 만약 같거나 작으면 거기부터 끝까지 재귀

# ** 문제가 만약에 A팀이 1일 때 B팀에 [2,3,5] 이런식이라면
# B팀에서 2를 내보내면 되는데
# 내가 짠 로직 속에서는 2가 맨 끝에 있어서 탐지를 못함. 그래서 fake 요소로 0을 넣어줌

answer = 0
arr = []

def p_search(s,e,num) :
    global answer 
    global arr
    if s>=e:
        return None

    mid = (s+e)//2
    mid_num = arr[mid]
    if mid_num > num:
        if arr[mid-1] <= num:
            del arr[mid]
            answer += 1 
            return arr
        else:
            return p_search(s,mid-1,num)
    elif mid_num < num:
        if arr[mid+1] > num:
            del arr[mid+1]
            answer += 1 
            return arr
        else:
            return p_search(mid+1,e,num)
    else:
        if arr[mid+1] > num:
            del arr[mid+1]
            answer += 1 
            return arr
        else:
            return p_search(mid+1,e,num)
        
def solution(A, B):
    global arr
    global answer
    
    B.sort()
    arr = [0] + B 
    
    for el in A:
        p_search(0,len(arr)-1,el)

    return answer
