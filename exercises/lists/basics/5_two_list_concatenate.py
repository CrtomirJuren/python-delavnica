list1 = ["Mo", "im", "j", "Fra"]
list2 = ["je", "e", "e", "nce"]

list_new = []
for i in range(4):
    item = list1[i] + list2[i]
    list_new.append(item)

stavek = ""
for i in range (4):
    stavek += list_new[i] + ' '

print(stavek)