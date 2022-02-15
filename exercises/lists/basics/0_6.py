"""
Exercise 10: 
Write a program in Python to remove duplicate items from a list.
"""

l = [2,3,4,5,2,4,5,3]
print(l)

result = []
for item in l:
    if item not in result:
        result.append(item)

print(result)