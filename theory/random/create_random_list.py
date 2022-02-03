# import module
import random

# seed is used to freeze randomness. 
# Everybody with the same seed, will get the same random result
SEED = 100
random.seed(SEED)

# random.sample(): list of random items of given length
samples = range(100, 200)

# select random items from this list
n_items = 10
list_random = random.sample(samples, n_items)

print(list_random)