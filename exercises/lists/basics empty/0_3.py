"""
Python program to square each element of a list.

# 1 programsko ustvari [1, 2, 3, 4] 
# 2 naredi funkcijo list_squared(), ki vrne rezultat
# 3 print result [1, 4, 9, 16]

def list_squared():
    return
"""

# definicija funckije
def list_squared(l):

    a = []
    for item in l:
        # result.append(item*item)
        a.append(item**2)

    return a

# program
l = list(range(1,5))
print(l)

result = list_squared(l)

print(result) #[1, 4, 9, 16]

