# OOP Object oriented programming

### Class
A class is like a set of instructions or blueprint for how to build many objects that share characteristics.

### Object
An object is a data type built according to specifications provided by the class definition.

### Instance
- A class is an object constructed from a blueprint
- An Instance is the blueprint for constructing class objects

### Encapsulation
Encapsulation is the process of designing a programmatic class using public and private methods and attrubutes to implement abstraction

### Abstraction
The idea of exposing only relevant data in a class interface, hiding private attrubutes and methods from user

### Attribute
attribute describes an object 

An attribute is a value(characteristic). Think of an attribute as a variable that is stored within an object.

### Method
method acts on an object and changes it.

A method is a set of instructions. Methods are functions, which are associated with an object. Any function included in the parent class definition can be called by an object of that class.

### What is the difference between a class method and an instance method?
- class method (cls), instance method(self)
- class methods must be decorated with "classmethod", instance methods dont
- class methods are used when the method does not need to know about the specific instance; instance methods are the opposite

### Polymorphism
The word polymorphism means having many forms. In programming, polymorphism means same function name (but different signatures) being uses for different types.

ko lahko metodo z istim imenom uporabiš na različnih objektih. vendar imajo enako strukturo. Metoda se bo pa za vsak objekt različno obnašala.

Polymorphism with class methods:
```python
class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
  
class USA():
    def capital(self):
        print("Washington, D.C")
    def language(self):
        print("English")
  
obj_ind = India()
obj_usa = USA()
for country in [obj_ind, obj_usa]:
    country.capital()
    country.language()
```

### Abstract Class
- iz tega razreda naj nebi direktno delal objekta
- je objekt iz katerega naj bi samo dedoval

```python
class Animal(object):
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should implement this abstract method")

class Monkey(Animal):
    def eat(self):
        print('eating bananas')

a = Monkey('jojo')
a.eat()
```
### Double under (Dunder) methods

without dunder override
```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Tom = Employee('Tom Lanister', 35)
print(Tom) #<__main__.Employee object at 0x000001F15D7AC7B8>
```

with dunder ovveride
print function shows string representation of an object. we can change this if we ovveride __str__ dunder method.
```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # string dunder method
    def __str__(self):
        return self.name + " has age of " + str(self.age)

Tom = Employee('Tom Lanister', 35)
print(Tom) # Tom Lanister has age of 35
```

## Simplest class
```python
#define class
class User():
    pass
#create an instances of this class
user1 = User()
user2 = User()

print(user1)  
# <__main__.User object at 0x039F0650>
print(user2)  
# <__main__.User object at 0x03B831B0>
```

# Example Class
```python
class User():
    # class attribute,class variable
    color = 'red' 
    # class method
    def __init__(self,first,last,age):
        print('a new user has been made!')
        # these are instance attributes
        self.first = first
        self.last = last
        self.age = age

#create an instance of this class
user1 = User('Joe','Smith',86)
user2 = User('Blanca','Lopez',41)
```

## class attributes
- Class attribute is something that is independant of the given instance.
- Its part of the class
- should be static, unchanged

```python
# this is BAD
# it will change all instances, all users
User.color = 'green'
# user1.color = 'green
# user2.color = 'green

# this is GOOD, it will change only instance
user1.color = 'green'

# add new instance to instance
user1.hasCar = True
```

```python
class User():
    # class attribute
    total_number = 0
    def __init__(self,first,last,age):
        print('new user!')
        User.total_number += 1
        # these are object attributes
        self.first = first
        self.last = last
        self.age = age

user1 = User('Joe','Smith',86)
user2 = User('Blanca','Lopez',41)

print(User.total_number) # 2
```
## Access specific atrribure on an instance 

```python
# instance.attribute_name
print(user1.first,user1.last)
print(user2.first,user2.last)
# Joe Smith
# Blanca Lopez
```

```python
```
## Creating a class
init method, gets called everytime you create an instance of the class

```python
class Vehicle:
    def __init__(self,make,model,year):
        print('a new user has been made!')
        #initialize class data
        self.make = make
        self.model = model
        self.year = year
#create an instance of this class
car = Vehicle('Honda','Civic',2017)
```

## class attributes
```python
class User():
    def __init__(self,first,last,age):
        print('a new user has been made!')
        # these are class attributes
        self.first = first
        self.last = last
        self.age = age

#create an instance of this class
user1 = User('Joe','Smith',86)
user2 = User('Blanca','Lopez',41)

print(user1.first,user1.last)
print(user2.first,user2.last)
```

## classic class recomendation
init method, gets called everytime you create an instance of the class

```python
#define class
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        
```

## Dunder method
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. ... Let's add a __repr__ method to represent our object.

## naming

internal use for the class
- _name 
change names with name mangling and hides for dificult access
- __name 
used for pyton specific methods
- \_\_name\_\_ 

## Name mangling

Python changes method names with double uderscore
```python
class Person:
    def __init__(self):
        self.name = "tony"
        self._secret = "hi!"
        self.__msg = "i like turtles"
        self.__lol = "hahahha"

#create an instance of this class
p = Person()

print(p.name)
print(p._secret)
#print(p.__msg) this doesnt work because two underscore
print(p._Person__msg) 
```

# Instance Attributes and methods

# Class Attributes
We can also define attributes directly on a class that are shared by all instancess of a calss and the class itself

- define a class variable: to count number of all Users

# Class methods
Class methods are methods(with the @classmethod decorator) 
that are not concerned with instances, but the class itself.

cls = short for class, standard nameing

```python
class Person:
    #....
    @classmethod    #this defines it is a class method, not an instance methods
    def from_csv(cls, filename):
        return cls(*params)

Person.from_csv(my_csv)
```

### \_\_repr\_\_

With "repr" we can control how we see the name of object
This method is one of several ways to provide a nicer string representation

repr = represent 
dunder/magic method

- WITHOUT REPR
```python
class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

j = User("judy", "steele", 18)
print(j)    #<__main__.User object at 0x038ED870>
```

- WITH REPR
```python
class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

j = User("judy", "steele", 18)
print(j)    #judy is 18
```