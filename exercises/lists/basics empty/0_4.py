"""
Python program to remove an empty element from a list.
- 1.) you can change original list
- 2.) you cant change original list

input
    l_in = ['Hello', 34, 45, '', 40]
output
    result = ['Hello', 34, 45, 40]
"""


l = ['Hello', 34, 45, '', 40]

""" RAM
1
2
3   ['Hello', 34, 45, '', 40]        ... l
4
5
6
7
8
9   ['Hello', 34, 45, '', 40]        .... l_2
"""
l_2 = l.copy()

for item in l_2:
    if item == '':
        l_2.remove(item)

print(l)
print(l_2)