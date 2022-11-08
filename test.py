import random
import timeit
from math import floor


def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2
        
# x = oddnumbers()

# for i in range(10):
    # print(next(x))
    # input()
    
####################################

def square(numbers):
    for n in numbers:
        yield n ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = square(numbers)

# print(squared_numbers)

# for x in squared_numbers:
#     print(x)

# print(next(squared_numbers))
# print(next(squared_numbers))
# print(next(squared_numbers))
# print(next(squared_numbers))
# print(next(squared_numbers))
# 
# print(next(squared_numbers))

#####################################

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# def data_list(n):
    # result = []
    # for i in range(n):
        # result.append(random.choice(numbers))
    # return result
# 
# def data_generator(n):
    # for i in range(n):
        # yield random.choice(numbers)
# 
# t_list_start = timeit.default_timer()
# rand_list = data_list(1_000_000)
# t_list_end = timeit.default_timer()
# 
# t_gen_start = timeit.default_timer()
# rand_gen = data_generator(1_000_000)
# t_gen_end = timeit.default_timer()
# 
# t_gen = t_gen_end - t_gen_start
# t_list = t_list_end - t_list_start
# 
# print(f"List creation took {t_list} Seconds")
# print(f"Generator creation took {t_gen} Seconds")
# 
# print(f"The generator is {floor(t_list / t_gen)} times faster")
# 
######################################

##### Find the most frequent element in a list #####

# test = [6, 2, 3, 5, 6, 7, 2, 2, 3, 4, 9, 2]
# most_frequent = max(set(test), key = test.count)
# 
# print(most_frequent)
 
######################################
