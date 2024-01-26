# example : 1

# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# here tuple and string are iterable containter which we can get from iterator
"""
string = "banana"
tup = ("adnd", "dkskj", "wokkk")

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

iter = iter(tup)

print(next(iter))
print(next(iter))
"""


# example : 2

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""
class BashSquare:
    def __init__(self, inp_data):
        self._data = inp_data
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._data):
            if isinstance(self._data[self._index], int):
                x = self._data[self._index]**2
                self._index += 1
                return x
            else:
                raise TypeError
        else:
            raise StopIteration

class Square:
    def __new__(cls, data_item : list = None):
        if data_item != None:
            sq = BashSquare(data_item)
            sq_obj = iter(sq)
            res = []
            for i in sq_obj:
                res.append(i)
            return res
        else:
            print(f"TypeError: required 2 position argument (m,n), but 1 is given.")
            raise TypeError
                 
sq_res = Square([1,2])
print(sq_res)
"""


# learn about the generator and get diffence between iterator and generator, when use iterator and when use generator.

# example 1
"""
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

for i in PowTwoGen(5):
    print(i)
"""



# examples of lambda function 

# example : 1
"""
x = lambda a : a**2
print(x(2))

# example : 2
def square(bash_val):
    res = lambda pow_val : bash_val**pow_val
    return res

print(square(10)(2))
"""


# This is use to create the class and object

# example : 1
"""
class AB:
    def __init__(self):
        # use to initialized the value at class objeect creation.
        self.a = 10

    def __str__(self):
        # use to return user readable string in format of object.
        return "AB Class"

    def fun(self):
        return self.a

obj = AB()
print(obj.fun())
print(obj)
"""


# example 2
"""
class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f"{self.fname, self.lname, self.age}")

class Student(Person):
    def __init__(self, fname, lname, age) -> None:
        super().__init__(fname, lname)
        self.age = age
    
    def print_name(self):
        print(f"{self.fname, self.age}")

    # using the overloading in class
    #def print_name(self, date):
    #    print(f"{self.fname, self.lname, self.age, date}")


sobj = Student('John', 'Deo', 25)
sobj.print_name()
#sobj.print_name("12.04.2023")
"""

# example 3
"""
# this is the example related to operator overloading.
class Addition:
    def __init__(self, a=0, b=0) -> None:
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        return "({0}, {1})".format(self.a, self.b)

    def __add__(self, obj):
        x =  self.a + obj.a
        y = self.b + obj.b
        #print(Addition(x,y))
        return Addition(x,y)

    def __sub__(self, obj):
        x =  self.a - obj.a
        y = self.b - obj.b
        #print(Addition(x,y))
        return Addition(x,y)

p1 = Addition(2, 5)
p2 = Addition(3, 9)
print(p1+p2) 
print(p2-p1)
"""



# it used for decorator

# example 1
"""
def myfunc(func):
    x = 300
    def myinnerfunc():
        print(x)
        func()
    return myinnerfunc

@myfunc
def abc():
    print("True")

abc()
"""


# example 2
"""
def decor(func):
    # use  the decorator for check negetive values
    def check_val(*arg):
        if arg[0] < 0 or arg[1] < 0:
            print("it's negetive value.")
        else:
            func(arg[0], arg[1])
            
    return check_val
    
    
@decor
def addition(x,y):
    print(x,y)


addition(-1,-2)
"""



# use to learn about comprehension {list, set, tuple} in python 

# example 1
"""
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = [i for i in inp]
print(my_list)
"""

# example 2
"""
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = [n for n in inp if n%2==0]
print(my_list)
"""

# example 3
"""
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = [n for n in inp if n%2==0 for _ in range(n)]
print(my_list)
"""

# example 3
"""
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = [[i for i in range(n)] for n in inp if n%2==0]
print(my_list)
"""

# example 4
"""
# this is use for tuple comprehension
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = [tuple([i for i in range(n)]) for n in inp if n%2==0]
print(my_list)
"""

# example 5
"""
# this is use for set comprehension
inp = [1,2,8,1,3,4,5,6,6,6,7,8,9,10]

my_set = {i for i in inp}
print(my_set)
"""

# example 6
"""
# this is use for dictionary comprehension
inp1 = [1,2,3,4,5,6,7,8,9,10]
inp2 = [1,2,3,4,5,6,7,8,9,10]

my_list = {inp1_val:inp2_val for inp1_val, inp2_val in zip(inp1, inp2)}
print(my_list)
"""

# example 7
"""
inp = [1,2,3,4,5,6,7,8,9,10] 

my_list = list(map(lambda a : a%2==0, inp))
print(my_list)
"""

# example 8
"""
inp = [1,2,3,4,5,6,7,8,9,10]

my_list = list(filter(lambda a : a%2==0, inp))
print(my_list)
"""

# example 9
# this is use for generator comprehension
"""
inp = [1,2,3,4,5,6,7,8,9,10]
# here () in comprehension return the generator object
my_gen = (i*i for i in inp)
print(my_gen)
for val in my_gen:
    print(val)
"""



# here we will see about the  context manager

# content manager is the object which is define in a with statement
# it is used to managed all resourcs properly and autometically.

# there is three method in object  __init__(), __enter__() and __exit__()
# __enter__() : run before going inside the with_statement body and return any value or content manager object itself.
# __exit__() : it's called when with_statement body exits

# example 1
"""
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with OpenFile('./abc', 'w') as f:
    f.write("this is context manager")

print(f.closed)
"""

# example 2
"""
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


with open_file('./abc', 'w') as f:
    f.write("this is context manager")

print(f.closed)
"""

