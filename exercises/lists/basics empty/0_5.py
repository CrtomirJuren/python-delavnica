"""
Exercise 8: 
    Write a program to display items from 1-20 
    that are divisible by 5.

    input
        l = [1,2,..,20]
    output
        l = [5, 10, 15, 20]
"""

### your solution here
# modulo ..ostanek .. %

l = list(range(1,21))
# print(l)

a = []
for item in l:
    ostanek = item % 5
    
    if not ostanek:
        print(item)
        # l.remove(item)
        a.append(item)

print(a)
