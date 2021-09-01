# 합병정렬 파이썬으로 구현해보기 

def merge_sort(lists):
  if len(lists) == 0:
    return []
  if len(lists) == 1:
    return lists
  else:
    if len(lists) == 2:
      left = lists[:1]
      right = lists[1:]
    else:
      l = (len(lists)//2) + 1
      left = lists[:l]
      right = lists[l:]
    left_list = merge_sort(left) 
    right_list = merge_sort(right)

    result = []

    while True:

      if len(left_list) == 0 :
        result += right_list
        break
      elif len(right_list) == 0:
        result += left_list
        break

      if left_list[0]>right_list[0] :
        result.append(right_list[0])
        right_list.pop(0)
      elif left_list[0]<right_list[0] :
        result.append(left_list[0])
        left_list.pop(0)
      else:
        result.append(left_list[0])
        result.append(right_list[0])
        left_list.pop(0)
        right_list.pop(0)

    return result 