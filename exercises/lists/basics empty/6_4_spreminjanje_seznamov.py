""" 6.4 spreminjanje seznamov """

""" negativne elemente spremeni v pozitivne """

# ---------------- NE DELUJE ------------------------
# kvadriraj elemente v seznamu
seznam = [-1, 10, -5, 15, 0, -3]
for element in seznam:
    element = abs(element)
    print(element)

print(seznam)

# ------ DELUJE AMPAK SPREMENI ORIGINAL ----------------
# seznam = [-1, 10, -5, 15, 0, -3]
# for index, element in enumerate(seznam):
#     seznam[index] = abs(element)
#     print(element)

# print(seznam)


# # -------- DELUJE IN NE SPREMENI ORIGINALA ---------
# seznam = [-1, 10, -5, 15, 0, -3]
# seznam_nov = []
# for index, element in enumerate(seznam):
#     seznam_nov.append(abs(element))
#     print(element)

# print(seznam)
# print(seznam_nov)

