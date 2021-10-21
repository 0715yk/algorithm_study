import math

def check(n):
    if (n & (n - 1)):
        return False
    else:
        return True
    
def int_to_bin(num):
    return list(bin(num).split('b')[1])

def solution(numbers):
    # DP 로풀어보자
    answer = []
    for el in numbers:
        if el % 2 == 0:
            # 짝수면 끝에 1만 붙이면됨
            answer.append(el+1)
        else:
            if check(el+1):
                answer.append(el+(2**(int(math.log2(el+1))-1)))
            else:
                std = int_to_bin(el)
                for j in range(len(std)-1, -1, -1):
                    if j == 0:
                        std = ["0b"] + std 
                    elif std[j] == "0":
                        std[j] = "1"
                        std[j+1] = "0"
                        break
                answer.append(int("0b"+"".join(std),2))
    return answer

    # numbers의 정수를 받아서
    # 비트단위로 바꾼다
    # 그 다음에 그것보다 작은 수의 비트값과 그 비트를
    # 하나하나씩 비교해가되 다른개 2개 이하면 break 걸고 해당 배열을 answer에 추가한다
    
    # 근데 정수를 어떻게 비트로 바꾼담?
    # 16비트로 표현한 것 같음
    # 아래처럼 풀면 시간초과
    
# def int_to_bin(num):
#     return list(bin(num).split('b')[1])
#     for el in numbers:
#         now = el
#         std = int_to_bin(el)
        
#         while True:
#             now += 1
#             arr = int_to_bin(now)
#             cnt = 0
            
#             if len(arr) > len(std):
#                 std = ["0" for i in range(len(arr)-len(std))] + std
                
#             for idx in range(len(arr)):
#                 if arr[idx] != std[idx]:
#                     cnt += 1 
                    
#             if cnt <= 2:
#                 answer.append(now)
#                 break

# DP 로 규칙을 찾은 듯 했으나 실패 (2차시도)

# def check(n):
#     if (n & (n - 1)):
#         return False
#     else:
#         return True
    
    # l = [True,True,True,False]
    # for el in numbers:
    #     if l[el % 4]:
    #         answer.append(el+1)
    #     else:
    #         if check(el+1):
    #             answer.append(el+(2**(int(math.log2(el+1))-1)))
    #         else:
    #             answer.append(el+2)