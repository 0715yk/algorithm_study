def solution(s):
    answer = ''
    d = {
        'zero' : '0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    s += "#"
    word = ""
    for el in list(s):
        try:
            answer += str(int(el))
        except:
            word += el
            try:
                if d[word] :
                    answer += d[word]
                    word = ""
            except:
                pass
    return int(answer)