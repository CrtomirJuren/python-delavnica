" Zgled 20. napiši program ki se sprehodi čez celoten seznam in izpiše vrednost in index najmanjšega elementa """
import random

def create_random_list():
    SEED = 101
    random.seed(SEED)
    seznam = random.sample(range(10, 30), 10)
    return seznam

seznam = create_random_list()
print(seznam)

# [28, 16, 27, 21, 24]
element_min = seznam[0]
index_min = 0

for index, element in enumerate(seznam):
    # ali je novi element manjši od najmanjšega
    # če je, potem ga shrani
    if element <  element_min:
        element_min = element
        index_min = index

# pythonic
element_min = min(seznam)
index_min = seznam.index(element_min)

print(element_min, index_min)
# print(f'najmanjsi element seznama {seznam} = {element_min}, indeks = {index_min} ')