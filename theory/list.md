# Lists

- Lists is a mutable sequence type (items can be changed)

## Initializing

- 1st variant - manual
```python
items = []
items = [1, 2, 3]
```

- 2nd variant - range( ) and convert to list
```python
items = list(range(4))     # [0, 1, 2, 3]
items = list(range(1,4))   # [1, 2, 3]
items = list(range(1,4,2)) # [1, 3]
```

-3rd variant - for loop
```python
l = []
for i in range(3):
    l.append(i)
# [1, 2, 3]
```

-4th variant - list comprehansion
```python
l = [x for x in range(3)]
# [1, 2, 3]

pow2 = [2 ** x for x in range(10)]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

pow2 = [2 ** x for x in range(10) if x > 5]
# [64, 128, 256, 512]
```

## Accessing values by indexes
- forward, positive indexing
```python
items = [1, 2, 3]
items[0] # 1
items[1] # 2
items[2] # 3
items[3] # IndexError
```

- backward, negative indexing
```python
items[-1] # 3
items[-2] # 2
items[-3] # 1
```

### Check if a Value is in a List
```python
friends = ["Ashley","Matt","Michael"]
```

```python
"Ashley" in friends # True
"Colt"   in friends # False
```

### Accessing all values

for loop = preffered
```python
for x in friends:
    print(x)
```

list comprehansion
```python
[ print(x) for x in friends]
```

### Accessing all values - while loop
```python
i=0
while i < len(friends):
    print(f"index {i} has a value {friends[i]}")
    i += 1
# index 0 has a value "Ashley"
# index 1 has a value "Matt"
# index 2 has a value "Michael"
```
### concatenating, repeating: adding
```python
odd = [1, 3, 5]

print(odd + [9, 7, 5]) # [1, 3, 5, 9, 7, 5]

print(["re"] * 3) # ['re', 're', 're']
```

## Methods

|  Methods | Descriptions|
| ---: | :-- |
| append() | adds an element to the end of the list|
| extend() | adds all elements of a list to another list|
| insert() | inserts an item at the defined index|
| remove() | removes an item from the list|
| pop()	   | returns and removes an element at the given index|
| clear()  | removes all items from the list|
| index()  | returns the index of the first matched item|
| count()  | returns the count of the number of items passed as an argument|
| sort()   | sort items in a list in ascending order|
| reverse()| reverse the order of items in the list|
| copy()   |returns a shallow copy of the list|


- append
adds single item
```python
list_1 = [1,2,3,4]
list_1.append(5)
print(list_1) # [1,2,3,4,5]
```

### extend
adds multiple items
```python
list_1 = [1,2,3]
list_1.extend([5,6,7])
print(list_1) # [1,2,3,4,5,6,7]
```

### insert
adds with index offset
```python
list_1 = [1,2,3]
list_1.insert(2, 'Hi!')
print(list_1) # [1,2,'Hi!',3,4]
```
### insert at end
adds with index offset
```python
list_1 = [1,2,3]
list_1.insert(len(list_1), 'Hi!')
print(list_1) # [1,2,3,4,'Hi!']
```
### clear
removes all items from the list
```python
list_1 = [1,2,3]
list_1.clear()
print(list_1) # []
```
### pop: 
```python
list_1 = [1,2,3]
list_1.pop() #removes last item 4
removed_item = list_1.pop(1) #removes second item 2 and stores to variable
print(list_1) # [1,3]
```
### remove
search first item with the same value and removes it  
```python
list_1 = [1,2,4,4,4]
list_1.remove(4) #removes last item 4
print(list_1) # [1,2,4,4]
```

### index
returns the index of the specified item in the list  
```python
list_1 = [5,5,6,7,5,8,8,9,10]
list_1.index(5)  #0
list_1.index(5,1) #1 after index1
list_1.index(5,2) #4 after index2
list_1.index(8,6,8) #looking for 8 between index 6 and index 8

returns error
```

### count
counts duplicates in list  
```python
list_1 = [5,5,6,7,5,8,8,9,10]
list_1.count(5)  #3 times
```

### reverse
```python
list_1 = [1,2,3]
list_1.reverse()  #3 times
print(list_1) #[3,2,1]
```

### sort
```python
list_1 = [5,2,1,4,3]
list_1.sort()  
print(list_1) # [1,2,3,4,5]
```

```python
list_1 = [5,2,1,4,3]
list_1.sort(reverse = True)  
print(list_1) # [5,4,3,2,1]
```

### join: string method, converts list to string
```python
words = ['coding','is ','fun']

'',join(words) #'coding is fun'
```

## Slicing lists
```python
some_list[start:end:step]
```
## Slicing lists - first parameter start
```python
list_1 = [1,2,3,4]

-forward
list_1[1:] # [2,3,4]
list_1[3:] # [4]

-backward
list_1[-1:] # [4]
list_1[-3:] # [2,3,4]
```

## Slicing lists - second parameter end
```python
list_1 = [1,2,3,4]

-forward
list_1[:2] # [1,2]
list_1[:4] # [1,2,3,4]
list_1[1:3] # [2,3]

-backward
list_1[:-1] # [1,2,3]
list_1[1:-1] # [2,3]
```

## Slicing lists - third parameter step
```python
list_1 = [1,2,3,4,5,6]

-forward
list_1[1::2] # [2,4,6]
list_1[::2] # [1,3,5]

-backward
list_1[1::-1] # [2,1]
list_1[:1:-1] # [6,5,4,3]
list_1[2::-1] # [3,2,1]
```

## Reversing
```python
string = 'this is fun'
string[::-1] #'nuf si siht'
```

## Modifying slice
```python
numbers = [1,2,3,4,5]
numbers[1:3]=['a','b','c']
print(numbers) #[1,'a','b','c',2,3,4,5]
```

## Swapping values
```python
# [1,2,3,4,5]
i,j = 0, 1
numbers[i], numbers[j] = numbers[j], numbers[i]
```

## Nested Lists
```python
board = [['X','O','O'],
         ['O','X','O'],
         ['O','O','X']]
```

# Nested indexing
```python
board[0][0]
```

# LIST COPYING
```
10.59 sec (105.9 µs/itn) - copy.deepcopy(old_list)
10.16 sec (101.6 µs/itn) - pure Python Copy() method copying classes with deepcopy
1.488 sec (14.88 µs/itn) - pure Python Copy() method not copying classes (only dicts/lists/tuples)
0.325 sec (3.25 µs/itn)  - for item in old_list: new_list.append(item)
0.217 sec (2.17 µs/itn)  - [i for i in old_list] (a list comprehension)
0.186 sec (1.86 µs/itn)  - copy.copy(old_list)
0.075 sec (0.75 µs/itn)  - list(old_list)
0.053 sec (0.53 µs/itn)  - new_list = []; new_list.extend(old_list)
0.039 sec (0.39 µs/itn)  - old_list[:] (list slicing)
```