# Touples

## Grouping data

```python
>>> year_born = ("Paris Hilton", 1981)
```
This is an example of a data structure — a mechanism for grouping and organizing data to make it easier to use.

The pair is an example of a tuple. Generalizing this, a tuple can be used to group any number of items into a single compound value. Syntactically, a tuple is a comma-separated sequence of values. Although it is not necessary, it is conventional to enclose tuples in parentheses:
```python
>>> julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
```

Tuples are useful for representing what other languages often call records — some related information that belongs together, like your student record. There is no description of what each of these fields means, but we can guess. A tuple lets us “chunk” together related information and use it as a single thing.

Tuples support the same sequence operations as strings. The index operator selects an element from a tuple.
```python
>>> julia[2]
1967
```
If we try to use item assignment to modify one of the elements of the tuple, we get an error:
```python
>>> julia[0] = "X"
TypeError: 'tuple' object does not support item assignment
```
So like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed.

Of course, even if we can’t modify the elements of a tuple, we can always make the julia variable reference a new tuple holding different information. To construct the new tuple, it is convenient that we can slice parts of the old tuple and join up the bits to make the new tuple. So if julia has a new recent film, we could change her variable to reference a new tuple that used some information from the old one:

```python
>>> julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
>>> julia
("Julia", "Roberts", 1967, "Eat Pray Love", 2010, "Actress", "Atlanta, Georgia")
```
To create a tuple with a single element (but you’re probably not likely to do that too often), we have to include the final comma, because without the final comma, Python treats the (5) below as an integer in parentheses:
```python
>>> tup = (5,)
>>> type(tup)
<class 'tuple'>
>>> x = (5)
>>> type(x)
<class 'int'>
```

## Touple unpacking
-  Example
```python
def sum_all_values(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    print(total_sum)

sum_all_values(1,2,3)       #without unpacking
sum_all_values(*[1,2,3])    #with unpacking
```
Problem:function doenst work for list [1,2,3]. We need to unpack it, item by item

Unpacking means, items are read out of list one by one

## Glossary

- data structure
An organization of data for the purpose of making it easier to use.

- immutable data value
A data value which cannot be modified. Assignments to elements or slices (sub-parts) of immutable values cause a runtime error.

- mutable data value
A data value which can be modified. The types of all mutable values are compound types. Lists and dictionaries are mutable; strings and tuples are not.
tuple

- An immutable data value that contains related elements. Tuples are used to group together related data, such as a person’s name, their age, and their gender.
- 
- tuple assignment
An assignment to all of the elements in a tuple using a single assignment statement. Tuple assignment occurs simultaneously rather than in sequence, making it useful for swapping values.