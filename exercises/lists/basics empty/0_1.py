""" Exercise 1
    Write a program to create a list with random data types elements.
    
    input
        l = [0, "hello", 3.14, [1,2,3],{'ime':'John'}]
    output
        result = [<class 'int'>, <class 'str'>, <class 'float'>, <class 'list'>, <class 'dict'>]

for item in list:
    # do something
"""


l = [0, "hello", 3.14, [1,2,3],{'ime':'John'}]
print(l)

### your solution here

result = []

for item in l:
    # print(item, type(item))
    tip_itema = type(item)
    result.append(tip_itema)

print(result)
# print(result) [<class 'int'>, <class 'str'>, <class 'float'>, <class 'list'>, <class 'dict'>]

# ali so vsi element različni....