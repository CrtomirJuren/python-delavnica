"""
Exercise 2: 
    Write a program to print all the elements
    of a list in single line.
    input:  
        l = [0, 1, 2, 3, 4]
    output:
        result:  0 1 2 3 4
"""

### your solution here
# l = [0, 1, 2, 3, 4]
l = list(range(0,5))
print(l)

result = ''
presledek = ' '

for item in l:
    # str = str + int
    result = result + str(item) + presledek

print(result)