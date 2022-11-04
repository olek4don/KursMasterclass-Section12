def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2
        
x = oddnumbers()

# for i in range(10):
    # print(next(x))
    # input()
