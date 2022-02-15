"""
Exercise 13:
Write a program in Python to filter
odd and even number from a list.
"""

# input
l = [1,2,3,23,46,76,89]
# output sode [2,46,76]
# output lihe [1,3,23,89]

sode = []
lihe = []

for item in l:
    ostanek = item%2
    if ostanek:
        lihe.append(item)
    else:
        sode.append(item)

print('sode', sode)
print('lihe', lihe)