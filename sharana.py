list1=[11,21,31,91,99]
element=101
if position>len(list1):
  print('cannot perform the operation')
 else:
    list2=[None]*(len(list1)-1)
    for i in range(position):
      list2[i]=list1[i]
    for i in range(position,len(list2)):
      list2[i]=list1[i+1]
    print(list2)
