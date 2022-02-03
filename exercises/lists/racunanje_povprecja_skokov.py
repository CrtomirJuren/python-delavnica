"""
script that calculates ski jump avarage length
"""
import random
import matplotlib.pyplot as plt

# randomly generated list

SEED = 101
random.seed(SEED)
seznam = random.sample(range(100, 200), 7)
# print(seznam)

# # uredi seznam od najmanjše do največje št
# # seznam.sort()
# # print(seznam[3])

# seznam.append(145)

# print(seznam)

# print(seznam.count(145))

#  1 2 3 4 5
# avg = (1+2+3+4+5)/st_elementov

vsota_dolzin = sum(seznam)
st_dolzin = len(seznam)
avg_length = vsota_dolzin / st_dolzin
avg_length_list = [avg_length] * 7
print(avg_length) 
print(avg_length_list)

minumum = min(seznam)
minimum = [minumum] *7
maximum = max(seznam)
maximum = [maximum] *7
# [  0,   1,   2,   3,   4,   5,   6]
# [174, 124, 169, 145, 159, 106, 184]

# x_os = [0,1,2,3,4,5,6]
x_os = list(range(7))

plt.plot(x_os, seznam)
plt.plot(x_os, avg_length_list)
plt.plot(x_os, minimum)
plt.plot(x_os, maximum)
plt.show()