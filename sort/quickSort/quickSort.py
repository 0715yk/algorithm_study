# 퀵정렬 구현하기 (Python)
def quick_sort(lists) :
  if len(lists) ==0 or len(lists)== 1:
    return lists 
  else:
    pivot = lists[0]
    ltp = []
    gtp = []
    for i in range(1, len(lists)):
      if lists[i]>pivot:
        gtp.append(lists[i])
      else:
        ltp.append(lists[i])
    return quick_sort(ltp) + [pivot] + quick_sort(gtp)