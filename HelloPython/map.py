# map,filter,zip and reduce
from functools import reduce


my_list = [1,2,3]
# your_list = [10,20,30]
# def multiplay_by2(item):
#     return item * 2
# print(list(map(multiplay_by2,my_list)))
# def only_odd(item):
#     return item % 2 != 0
# print(list(filter(only_odd,my_list)))
# print(list(zip(my_list,your_list)))
keys = ["first","last","location"] 
values = ["Justin","Liu","London"]
# for index in range(len(key)):print(index,keys[index],values[index])
for k, v in zip(keys,values):
    # print(f"{k}: {v}")

#  def accumulator(acc,item):
#     print( acc, item)
#     return acc + item
# print(reduce(accumulator,my_list,0))
# lambda function, they dont have name, action that need 
#  print(list(map(lambda item: item*2,my_list)))
# print(list(filter(lambda item: item % 2 != 0,my_list)))
# print(reduce(lambda acc, item: acc+item,my_list))

 