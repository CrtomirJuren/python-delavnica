"""
Python program to remove an empty element from a list.
"""

list_in = ['Hello', 34, 45, '', 40]
# result = ['Hello', 34, 45, 40]

for item in list_in:
    if not item:
        list_in.remove(item)

print(list_in)