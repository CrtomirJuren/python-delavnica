""" str 65 sprehajanje čez sezname z zanko for """

#2nd variant - range to list
seznam = list(range(3))
for element in seznam:
    print(element)


""" sprehanjanje čez indexe seznama """
seznam = ['rdeča', 'roza','modra','siva']

# 1 način
for index in range(len(seznam)):
    element = seznam[index]
    print(index, element)

# 2 način, elegantnejše
for index, element in enumerate(seznam):
    print(index, element)


