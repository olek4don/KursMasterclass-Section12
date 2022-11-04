# def gen_odd():
    # current, nnext = 1, 3
    # while True:
        # yield current
        # current, nnext = nnext, nnext + 2
        # 

def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2

def pi_series():
    odds = oddnumbers()
    approximation = 0   # set initial value to 0
    while True:     # infinite loop
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation
        

approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))

# odds = oddnumbers()

# for i in range(100):
    # print(next(odds))

# print(next(god))
# print(next(god))
# print(next(god))
# print(next(god))
# print(next(god))
