# Importing the ABC module for abstract base classes
from abc import ABC, abstractmethod

# Task 1
# Create a simple car class with brand and model attributes. 
# Add a method that displays the full name of the car.
class Car():
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

car1 = Car("Tesla", "Model S")
print("\nTask 1 - Creating a Car instance:")
print("Full name of the car:", car1)

# Task 2 
# Implement the bank accounts class with balance attributes and a transfer method that allows you to transfer funds between two accounts. 
# Use the isinstance(object, type) method.
class BankAccount():
    def __init__(self, balance) -> None:
        self.balance = balance
    def __str__(self) -> str:
        return f"{self.balance}"
    def transfer(self, account, amount):
        if isinstance(account, BankAccount):
            if self.balance >= amount:
                self.balance -= amount
                account.balance += amount
                print("Transaction completed")
            else:
                print("Insufficient funds")
        else:
            print("Enter a valid account")

account1 = BankAccount(1000)
account2 = BankAccount(2000)
print("\nTask 2 - Creating BankAccounts:")
print("Initial balances - Account 1:", account1, "Account 2:", account2)
account1.transfer(account2, 500)
print("Account 1 balance after transfer:", account1)
print("Account 2 balance after transfer:", account2)

# Task 3
# Create a GeometricFigure class with the abstract method calculate_area(). 
# Then create two classes inheriting it: a square and a circle.
class GeometricFigure(ABC):
    def __init__(self, side):
        self.side = side
    @abstractmethod
    def calculate_area(self):
        pass

class Square(GeometricFigure):
    def __init__(self, side):
        super().__init__(side)
    def calculate_area(self):
        return self.side**2

class Circle(GeometricFigure):
    def __init__(self, side):
        super().__init__(side)
    def calculate_area(self):
        return 3.14 * self.side ** 2

square1 = Square(4)
circle1 = Circle(5)
print("\nTask 3 - Creating Square and Circle instances:")
print("Side length of square:", square1.side)
print("Radius of circle:", circle1.side)
print("Area of square:", square1.calculate_area())
print("Area of circle:", circle1.calculate_area())

# Task 4
# Define a metaclass that verifies that all classes in the module 
# have a name that starts with a capital letter.
class MetaCheck(type):
    def __new__(cls, name, bases, dct):
        if name[0] >= "A" and name[0] <= "Z":
            print("Creating class:", name)
            return super().__new__(cls, name, bases, dct)
        else:
            print(f"Class name should begin with an uppercase letter, class '{name}' not created")

print("\nTask 4 - Using MetaCheck metaclass to check the first letter:")
# The class "notCreated" does not meet the condition of MetaCheck, so it is not created.
class notCreeated(metaclass=MetaCheck):
    pass
class Created(metaclass=MetaCheck):
    pass


# Task 5
# Create a person class with first and last name attributes. 
# Create a metaclass that adds an auto-generated ID for each instance.
class MetaId(type):
    _id_counter = 0
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance

class Person(metaclass=MetaId):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# Usage example
person1 = Person("John", "Doe")
person2 = Person("Alice", "Smith")
person3 = Person("Emma", "Johnson")
print("\nTask 5 - Generating auto-generated IDs:")
print("Person:", person1.first_name, person1.last_name, "ID:", person1.id)
print("Person:", person2.first_name, person2.last_name, "ID:", person2.id)
print("Person:", person3.first_name, person3.last_name, "ID:", person3.id)


# Task 6
# Write a complex class that allows you to add complex numbers
class ComplexNumber():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
       return f"Complex number: {self.real} + i{self.imag}"
    def sum(self, z):
        if isinstance(z, ComplexNumber):
            result = ComplexNumber(self.real, self.imag)
            result.real += z.real
            result.imag += z.imag
            return result
        else:
            print("We can only add two complex numbers")

z1 = ComplexNumber(3, 7)
z2 = ComplexNumber(2, 4)
print("\nTask 6 - Creating ComplexNumbers:")
print("Complex number z1:", z1)
print("Complex number z2:", z2)
z_result = z1.sum(z2)
print("Result of complex number addition:", z_result)

# Task 7
# Create an abstract animal class with the abstract method sound (). 
# Then create two classes inheriting it: dog and cat.
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")


cat = Cat()
dog = Dog()
print("\nTask 7 - Creating Animal instances with abstract class Animal:")
cat.sound()
dog.sound()


# Task 8
# Define a metaclass that limits the number of instances of a given class to one.
class MetaOne(type):
    _counter = 0
    def __call__(cls, *arg, **kwarg):
        if cls._counter == 0:
            isinstance = super().__call__(*arg, **kwarg)
            cls._counter +=1
            return isinstance
        else:
            return "Too much instances"

class Bird(metaclass = MetaOne):
    pass
class Fish(metaclass = MetaOne):
    pass

print("\nTask 8 - Limiting the number of instances:")
bird1 = Bird()
bird2 = Bird()
print("Bird instances:", bird1)  
print(bird2) # Output: Too many instances
fish1 = Fish()
fish2 = Fish()
print("Fish instances:", fish1) 
print(fish2) # Output: Too many instances


# Task 9
# Implement the abstract container class with the add_element() and remove_element () abstract methods. 
# Then create two inheriting classes: Stack and queue.
class Container(ABC):
    def __init__(self):
        self.elements = []
    @abstractmethod
    def add_element(self, el):
        pass
    @abstractmethod
    def remove_element(self):
        pass

class Stack(Container):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return " ".join(map(str, self.elements))
    def add_element(self, el):
        self.elements.append(el)
    def remove_element(self):
        if len(self.elements) == 0:
            return "Stack is empty"
        else:
            self.elements.pop()

class Queue(Container):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return " ".join(map(str, self.elements))
    def add_element(self, el):
        self.elements.append(el)
    def remove_element(self):
        if len(self.elements) == 0:
            return "Queue is empty"
        else:
            self.elements.pop(0)

stack = Stack()
stack.add_element(6)
stack.add_element(7)
stack.add_element(8)
print("\nTask 9 - Creating Stack instance:")
print("Stack contents after adding elements:", stack)
stack.remove_element()
print("Stack contents after removing an element:", stack)

queue = Queue()
queue.add_element(6)
queue.add_element(7)
queue.add_element(8)
print("\nTask 9 - Creating Queue instance:")
print("Queue contents after adding elements:", queue)
queue.remove_element()
print("Queue contents after removing an element:", queue)

# Task 10
# Define a metaclass that automatically adds the @property decorator to all properties in the class.
class MetaProperty(type): 
    def __new__(cls, name, bases, dct): 
        processed_dct = {}
        for key, value in dct.items(): 
            if not isinstance(value, property) and not key.startswith("__") and not callable(value): 
                processed_dct[key[1:]] =  property(lambda self, k=key: getattr(self, k),
                                                   lambda self, value, k=key: setattr(self, k, value))    
            else:
                processed_dct[key] = value
        return super().__new__(cls, name, bases, processed_dct) 

class MyClass(metaclass=MetaProperty): 
    _x = 0
    def __init__(self, x): 
        self._x = x 

obj = MyClass("World")
print("\nTask 10 - Adding the @property decorator to all properties:")
print("Initial value of x attribute:", obj._x)
print("Value of x attribute after applying @property decorator:", obj.x)

# Task 11
# Create a metaclass that automatically generates __str__ methods for all attributes of a given class.
class StrMeta(type):
    def __new__(cls, name, bases, dct):
        def generate_str_method(obj):
            return '\n'.join(f"{attr}: {getattr(obj, attr)}" for attr in obj.__dict__.keys() if not attr.startswith("__"))

        dct['__str__'] = lambda self: generate_str_method(self)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=StrMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        pass

obj1 = MyClass("Alice", 30)
print("\nTask 11 - Generating __str__ methods for all attributes with StrMeta metaclass:")
print(obj1)

