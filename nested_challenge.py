# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.
 
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

table = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(table)

for table in [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]:
    print(table)  

table2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(table2)

for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):   # generator expression
    print(x, y)  
