" Zgled 20. napiši program ki se sprehodi čez celoten seznam in izpiše vrednost in index najmanjšega elementa """
import random

SEED = 101
random.seed(SEED)
seznam = random.sample(range(10, 30), 5)
print(seznam)

# 2 način, elegantnejše

# inicializiramo z prvim elementom
element_min = seznam[0]
index = 0
index_min = 0

for element in seznam:
    print(index, element)
    if element < element_min:
        element_min = element
        index_min = index
    # index se poveča z vsako iteracijo for zanke
    index += 1

print(f'najmanjsi element seznama {seznam} = {element_min}, indeks = {index_min} ')