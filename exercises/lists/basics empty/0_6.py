"""
Exercise: 
    Write a program in Python to remove duplicate items from a list.

    intput
        list_in = [2,3,4,5,2,4,5,3]
    output
        result = [2, 2, 3, 4, 5]
"""
### your solution here
l = [2,2,3,4,5,2,4,5,3]
print(l)

result = []
for item in l:
    
    if item not in result:
        print(item)
        result.append(item)

print(result) #[2, 3, 4, 5]

"""
1 2 -> result.append(item)
2 2 -> ne sme se izvesti
3 3 -> result.append(item)
"""