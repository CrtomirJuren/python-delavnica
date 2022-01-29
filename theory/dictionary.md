# Dictionary
A data structure that consists of key value pairs
Keys describe data, value represents data

## Creating, initializing
Example 1 create a dictionary with var={}
```python
dictionary = {
    "name": "Janez",
    "surname": "Novak",
    "language": "Python",
    owns_dog=True
}
```

Example 2 create a dictionary with var=dict()
```python
dictionary= dict(name="Janez", surname="Novak", language="Python", owns_dog=True)
```

## Accessing values
```python
dictionary["name"]
```

## Iterating dictionaries

### Accessing values
```python
Using .values()

for value in dictionary.values():
    print(value)
```

```python
Using .keys()

for key in dictionary.keys():
    print(key)
```

- Accessing key-value pair. Using .items()
```python
for key,value in dictionary.items():
    print(f'key is {key}, value is {value}')
```

### Accessing value Example
```python
#Calculate sum of all donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

#version 1: using lambda
total_donations = sum(donation for donation in donations.values())

#version 2: using python sum function
total_donations = sum(donations.values())
```

### Testing for existance

- Does a dictionary have a key?
```python
"name" in dictionary #True
"phone" in dictionary #False
```

- Does a dictionary have a value?
```python
"Crtomir" in dictionary.values() #True
"Nope!" in dictionary.values() #False
```
## Dictionary Methods
```python
clear: Clears all the keys and values

d = dict(a=1,b=2,c=3)
d.clear #d={}
```
```python
copy: makes a copy

d = dict(a=1,b=2,c=3)
c = d.copy
c == d #true - same values
c is d #false - different memory positions
```

fromkeys: creates key-value pairs from comma separated values:
Always use a list, so not creating errors.
```python
{}.fromkeys(["a"],"b") #{"a":"b"}
{}.fromkeys(["email"],"unknown") #{"email":"unknown"}
{}.fromkeys(["a"],[1,2,3,4]) #{"a":[1,2,3,4]}
```

fromkeys example: initialize new user with None
```python
new_user = {}.fromkeys(["name","score","email"],None)
```

get: retrieves a key in a n object and return None instead of a KeyError
if the key doesnt exist
```python
d = dict(a=1,b=2,c=3)
#classical way, via key
d["a"] #1
d["g"] # KeyError

#new way, via .get[] method
d.get["a"] #1
d.get["b"] #2
d.get["g"] #None
```

pop:
takes a single argument correspoding to a key and removes that key-value pair from the dictionary. Returns the value correspoding to the key that was removed
```python
d = dict(a=1,b=2,c=3)
d.pop() #TypeError: argument expected
d.pop("a") #1
d # {"c":"3","b":"2"}
```

popitem:
removes a random key in a dictionary
```python
d = dict(a=1,b=2,c=3)
d.popitem() # ("d",4)
d.popitem("a") #TypeError: popitem takes no arguments
```

update:
updates key and values in a dictionary with another set of key value pairs
```python
first = dict(a=1,b=2,c=3)
second = {}

second.update(first)
second # {"a":"1", "b":"2", "c":"3"}
```

## Dictionary Access

## Dictionary unpacking