list1 = ["Mo", "im", "j", "Fra"]
list2 = ["je", "e", "e", "nce"]

zlog1 = list1[0] + list2[0]
zlog2 = list1[1] + list2[1]
zlog2 = list1[2] + list2[2]

# expected result
# stavek = 'Moje ime je France'
# zlog = list1[3]
# print(zlog)ž
stavek = ''
# ------------ PREPROST NAČIN ----------
# for i in range(len(list1)):
#     zlog1 = list1[i]
#     zlog2 = list2[i]

#     stavek += zlog1 + zlog2 +' '

stavek += '.'
print(stavek)



# print(stavek)


# -------- NAPREDNI NAČIN, ELEGANTNEJŠE ----------
# stavek = ''
# for element in zip(list1, list2):
#     stavek += ''.join(element) + ' '
# print(stavek)
