my_list = [5,4,3]
# print(list(map(lambda item: item ** 2,my_list)))
#  List Sorting
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
# print(a)





# list,set,dictionary
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
# print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
# print(squares)

# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)
# list set dict
my_num = [num ** 2 for num in range(0,21)]
# print(my_num)
# even_num = list(filter(lambda item: item % 2 == 0,my_num))
# print(even_num)
my_set = {set for char in 'hello'}
my_num2 = [num ** 2 for num in range(0,21) if num % 2 ==0]
print(my_num2)
my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)