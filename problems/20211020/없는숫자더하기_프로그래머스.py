def solution(numbers):
    return sum(list(set([i for i in range(0,10)]) - set(numbers)))