# def generator_function(num):
#     for i in range(num):
#         yield i
# for item in generator_function(100):
#     print(item)
# g = generator_function(1)
# next(g)
# print(next(g))
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break
special_for([123])
