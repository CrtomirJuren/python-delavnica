list1 = ["Mo", "im", "j", "Fra"]
list2 = ["je", "e", "e", "nce"]

# ------------ PRVI NAČIN ----------
# list_new = []
# for i in range(4):
#     item = list1[i] + list2[i]
#     list_new.append(item)

# for i in range(4):
#     item = list1[i] + list2[i]
#     list_new.append(item)

# stavek = ""
# for i in range (4):
#     stavek += list_new[i] + ' '

# print(stavek)


# -------------DRUGI NAČIN, ELEGANTNEJŠE ----------
# print(list(zip(list1, list2)))
# stavek = ''
# for element in zip(list1, list2):
#     stavek += ''.join(element) + ' '
# print(stavek)
