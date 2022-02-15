"""
Exercise 2: Write a program to print all the elements
 of a list in single line.
"""

l = list(range(5))

# l = [str(item) for item in l]

print(l)

result = ''
for item in l:
    item = str(item)
    result += item + ' '

print(result)

# result
# 0 1 2 3 4