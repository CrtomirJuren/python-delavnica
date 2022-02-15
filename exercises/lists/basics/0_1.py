""" Exercise 1: 
Write a program to create a list with random data types elements.
"""

l = [0, "hello", 3.14, [1,2,3],{'ime':'John'}]


result = [type(item) for item in l]

# [<class 'int'>, <class 'str'>, <class 'float'>, <class 'list'>, <class 'dict'>]
print(result) 