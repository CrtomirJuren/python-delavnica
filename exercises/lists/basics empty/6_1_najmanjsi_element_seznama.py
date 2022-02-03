" Zgled 20. napiši program ki se sprehodi čez celoten seznam in izpiše vrednost in index najmanjšega elementa """
import random

SEED = 101
random.seed(SEED)
seznam = random.sample(range(10, 30), 5)
print(seznam)



# TAK REZULTAT ŽELIMO
# print(f'najmanjsi element seznama {seznam} = {element_min}, indeks = {index_min} ')