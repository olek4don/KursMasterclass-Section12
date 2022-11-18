# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit

fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

x = fact(130)
"""
factorial_test = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(130)
"""

print(timeit.timeit(fact_test, number=10000))
print(timeit.timeit(factorial_test, number=10000))


####### my incorrect solutions #######
# setup = """\
# gc.enable()
# n = 10000    
# """


# fact = """\
# fact_1 = [f * (f + 1) for f in range(2, n + 1) if n > 1] 
# """

# factorial ="""\
# fact_2 = [n * (n - 1) if n > 1 else n == 1 for i in range(n, 1, -1)]
# """
# result_1 = timeit.timeit(fact, setup, number=1000)
# result_2 = timeit.timeit(factorial, setup, number=1000)


# print(f"Factorial nr 1: {result_1}")
# print(f"Factorial nr 2: {result_2}")
