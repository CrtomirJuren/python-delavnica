""" str 65 sprehajanje čez sezname z zanko for """

#2nd variant - range to list
# index = 0
# # seznam = list(range(3))
# seznam = ['a','b','c']
# for element in seznam:
#     print(f'element = {element}, index = {index}')
#     index += 1

# """ sprehanjanje čez indexe seznama """
seznam = ['rdeča', 'roza','modra','siva']

# print(len(seznam))
# # # 1 način
# for index in range(len(seznam)):
#     element = seznam[index]
#     print(index, element)

# # 2 način, elegantnejše
# print(list(enumerate(seznam)))

# for element in enumerate(seznam):
    # print(element)

for index, element in enumerate(seznam):
    print(f'index = {index},  element = {element}')