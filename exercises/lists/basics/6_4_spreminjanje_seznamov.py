""" 6.4 spreminjanje seznamov """

""" negativne elemente spremeni v pozitivne """

# ---------------- ne deluje ------------------------
# kvadriraj elemente v seznamu
seznam = [-1, 10, -5, 15, 0, -3]
for element in seznam:
    element = abs(element)
    print(element)

print(seznam)

# -----------------------------------------------
seznam = [-1, 10, -5, 15, 0, -3]
for index, element in enumerate(seznam):
    seznam[index] = abs(element)
    print(element)

print(seznam)


# -------- kako ohraniti originalni seznam---------
seznam = [-1, 10, -5, 15, 0, -3]
seznam_nov = []
for index, element in enumerate(seznam):
    seznam_nov.append(abs(element))
    print(element)

print(seznam)
print(seznam_nov)
