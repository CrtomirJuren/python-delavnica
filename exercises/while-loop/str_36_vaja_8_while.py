# """
# Napiši program ki šteje od 0 do števila ki ga je vnesel uporabnik, vsa števila naj uporabnik tudi izpiše
# """

# n = int(input('vpiši število, do katerega želiš prešteti: '))
# i = 0

# # while i <= n:  # i <= 10 = True
# #     print('inside while',i <= n, i)
# #     i += 1 # i = i+1

# # print('outside of while', i <= n, i)
# # print('end of loop')

# # i = 0
# while True:  # i <= 10 = True
#     print('inside while',i <= n, i)
#     i += 1 # i = i+1
#     # i = 1

#     print('before break')

#     if i >= n: # i1,n=5, 1<=5, true
#         break

#     print('after break')










# n = int(input('vpiši število, do katerega želiš prešteti: '))

# maksimalno število je 100, minimum je pa 0

while True:
    n = int(input('vpiši število, do katerega želiš prešteti: '))

    if n<10:
        break