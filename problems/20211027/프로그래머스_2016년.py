def solution(a, b):
    month = 1 
    l = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = b
    
    while month < a:
        if month == 2:
            days += 29
            month += 1 
        else:
            if month <= 7:
                if month % 2 == 0:
                    days += 30
                else:
                    days += 31
            else:
                if month % 2 == 0:
                    days += 31
                else:
                    days += 30
            month += 1
            
    index = days % 7 
    answer = l[index-1]

    return answer