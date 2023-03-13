import random

list_size = int(input('Enter integer number : '))
base_list = [i for i in range(list_size)]
random.shuffle(base_list)

print(base_list)

#sequence = input('sort sequense (u or d) : ')

def merge_sort(list_a):
  if len(list_a) <= 1:
    return list_a

  center=len(list_a)//2
  list_left=list_a[:center]
  list_right=list_a[center:]
  print('def list_l: ',list_left,'list_r: ',list_right)
  list_left=merge_sort(list_left)
  list_right=merge_sort(list_right)

  idx = idx_l = idx_r = 0

  while (idx_l < len(list_left)) & (idx_r < len(list_right)):
    if list_left[idx_l] < list_right[idx_r]:
      list_a[idx] = list_left[idx_l]
      idx_l = idx_l+1
    else:
      list_a[idx] = list_right[idx_r]
      idx_r = idx_r+1
    idx = idx+1
  while idx_l < len(list_left):
    list_a[idx] = list_left[idx_l]
    idx_l = idx_l+1
    idx = idx+1
  while idx_r < len(list_right):
    list_a[idx] = list_right[idx_r]
    idx_r = idx_r+1
    idx = idx+1
  print('def list_a: ',list_a)
  return list_a

print('Ans : ',merge_sort(base_list))
