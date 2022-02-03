
# 1st variant - for loop and append
seznam = []
for element in range(9):
    seznam.append(element)
print(seznam)

#2nd variant - range to list
seznam = list(range(9))
print(seznam)

#3nd variant - list comprehansion
seznam = [x for x in range(9)]
print(seznam)

# vaja izsek prvih 3 elementov 0,1,2
print(seznam[:3])

# izsek, srednjih 3 elementov 3,4,5
print(seznam[3:6])

# izsek zadnjih 3 elementov elementa 6,7,8
print(seznam[-3:])

# vsak sodi element
print(seznam[::2])

# vsak lihi element
print(seznam[1::2])
