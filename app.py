### 1. Using self (Simple)

class Student:
    def __init__(self, name):  # Constructor with self and name
        self.name = name       # Assigning name to the instance using self

    def greet(self):           # Instance method
        print("Hello, my name is", self.name)  # Access instance variable

# Example
s = Student("Ali")  # Creating object
s.greet()           # Calling method, output: Hello, my name is Ali

### 2. Using cls (Simple)

class Counter:
    total = 0  # Class variable shared by all objects

    def __init__(self):
        Counter.total += 1  # Increment class variable

    @classmethod
    def show_total(cls):  # cls is used for class-level access
        print("Total:", cls.total)

# Example
c1 = Counter()  # total becomes 1
c2 = Counter()  # total becomes 2
Counter.show_total()  # Output: Total: 2


### 3. Public Variables and Methods (Simple)

class Dog:
    def __init__(self, name):
        self.name = name  # Public variable

    def bark(self):  # Public method
        print(self.name, "is barking!")

# Example
d = Dog("Buddy")
print(d.name)  # Output: Buddy
d.bark()       # Output: Buddy is barking!


### 4. Class Variables and Class Methods (Simple)

class School:
    school_name = "City School"  # Class variable

    @classmethod
    def change_name(cls, name):
        cls.school_name = name  # Changing class variable

# Example
print(School.school_name)     # Output: City School
School.change_name("Modern School")
print(School.school_name)     # Output: Modern School


### 5. Static Method (Simple)

class Math:
    @staticmethod
    def add(x, y):  # No self or cls needed
        return x + y

# Example
print(Math.add(3, 4))  # Output: 7

### 6. Constructor & Destructor (Simple)

class Laptop:
    def __init__(self):
        print("Laptop is on")  # Constructor called automatically

    def __del__(self):
        print("Laptop is off")  # Destructor called on delete

# Example
l = Laptop()  # Output: Laptop is on
del l         # Output: Laptop is off


### 7. Access Modifiers (Simple)

class Person:
    def __init__(self):
        self.name = "Ali"       # Public
        self._age = 20          # Protected (convention)
        self.__salary = 50000   # Private

p = Person()
print(p.name)            # Output: Ali
print(p._age)            # Output: 20 (not strictly protected)
print(p._Person__salary) # Output: 50000 (name mangling)


### 8. super() Function (Simple)

class Parent:
    def __init__(self):
        print("Parent Init")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Child Init")

c = Child()  # Output: Parent Init\nChild Init

### 9. Abstract Class (Simple)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Cat(Animal):
    def sound(self):  # Must override abstract method
        print("Meow")

c = Cat()
c.sound()  # Output: Meow


### 10. Instance Method (Simple)

class Car:
    def __init__(self, brand):
        self.brand = brand  # Instance variable

    def drive(self):
        print(self.brand, "is driving")

c = Car("Toyota")
c.drive()  # Output: Toyota is driving

### 11. Class Method (Simple)

class Box:
    count = 0  # Class variable

    @classmethod
    def increment(cls):
        cls.count += 1  # Modify class variable

Box.increment()
print(Box.count)  # Output: 1


### 12. Static Method (Simple)

class Temp:
    @staticmethod
    def c_to_f(c):  # No self/cls
        return (c * 9/5) + 32

print(Temp.c_to_f(0))  # Output: 32.0


### 13. Composition (Simple)

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an engine (composition)

c = Car()
c.engine.start()  # Output: Engine started


### 14. Aggregation (Simple)

class Teacher:
    def __init__(self, name):
        self.name = name

class ClassRoom:
    def __init__(self, teacher):  # Teacher passed from outside
        self.teacher = teacher

mr = Teacher("Mr. Ali")
room = ClassRoom(mr)
print(room.teacher.name)  # Output: Mr. Ali


### 15. MRO (Simple)

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Multiple inheritance
    pass

obj = D()
obj.show()  # Output: B (MRO: D -> B -> C -> A)

### 16. Function Decorator (Simple)

def msg(func):
    def wrapper():
        print("Welcome")
        func()
    return wrapper

@msg  # Decorator
def hello():
    print("Hello")

hello()  # Output: Welcome\nHello


### 17. Class Decorator (Simple)

def decorate(cls):
    cls.info = lambda self: "Decorated Class"
    return cls

@decorate
class Demo:
    pass

d = Demo()
print(d.info())  # Output: Decorated Class


### 18. Property Decorator (Simple)

class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

p = Product()
p.price = 100
print(p.price)  # Output: 100


### 19. callable() and __call__() (Simple)

class Doubler:
    def __call__(self, x):  # Makes object callable
        return x * 2

d = Doubler()
print(callable(d))  # Output: True
print(d(5))         # Output: 10

### 20. Custom Exception (Simple)


class MyError(Exception):
    pass

def check(n):
    if n < 0:
        raise MyError("Negative not allowed")

try:
    check(-1)
except MyError as e:
    print(e)  # Output: Negative not allowed


### 21. Custom Iterable (Simple)

class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        val = self.n
        self.n -= 1
        return val

for i in CountDown(3):
    print(i)  # Output: 3 2 1 0

