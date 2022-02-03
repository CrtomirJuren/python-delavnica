# Exercise 1: Reverse a list in Python
"""
OSNOVA PAZI !!!
new_list = my_list, you don't actually have two lists

MORAŠ NAREDITI NOV LIST
new_list = old_list.copy()
new_list = old_list[:]
new_list = list(old_list)
"""
list_original = [100, 200, 300, 400, 500]

def reverse_list_1(l:list):
    # pazi metoda spremeni originalni list !
    l_copy = l.copy()
    l_copy.reverse()
    return l_copy

def reverse_list_2(l:list):
    # ta način vrne kopijo lista
    return l[::-1]

list_result_1 = reverse_list_1(list_original)
print('list_result_1', list_result_1)

list_result_2 = reverse_list_2(list_original)
print('list_result_2', list_result_2)

# preveri ali so naloge pravilno narejene
assert list_original == [100, 200, 300, 400, 500]
assert list_result_1 == [500, 400, 300, 200, 100]
assert list_result_2 == [500, 400, 300, 200, 100]
