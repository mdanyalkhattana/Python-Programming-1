# ------------------------------------------------------------
# Basic Class Example for Understanding OOP in Python
# ------------------------------------------------------------

# Class is like a blueprint or template for creating objects
# Objects are real examples of that class.

class Car:
    # Constructor: automatically runs when a new object is created
    def __init__(self, brand, model, year):
        self.brand = brand      # Instance variable
        self.model = model
        self.year = year

    # Method: function inside a class
    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is now running.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model} engine has stopped.")

# Creating objects from the class
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

# Accessing object data
print("Car 1 Brand:", car1.brand)
print("Car 2 Model:", car2.model)

# Calling methods
car1.start_engine()
car2.stop_engine()



# ------------------------------------------------------------
# PYTHON OOP — FOUR PILLARS EXAMPLE
# Purpose: Demonstrate Encapsulation, Abstraction, Inheritance, and Polymorphism
# ------------------------------------------------------------

# -------------------------------
# 1️⃣ ENCAPSULATION
# -------------------------------
# Encapsulation means keeping data (variables) and methods (functions)
# together in one unit (class), and restricting direct access to them.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public attribute
        self.__balance = balance # Private attribute (cannot be accessed directly outside)

    # Public method to view balance safely
    def get_balance(self):
        return self.__balance

    # Public method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    # Public method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount")

# Creating object
acc = BankAccount("Danyal", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Current Balance:", acc.get_balance())

# Accessing private variable directly will cause an error
# print(acc.__balance)  # ❌ Not allowed (Encapsulation in action)

print("\n---------------------------------------")

# -------------------------------
# 2️⃣ ABSTRACTION
# -------------------------------
# Abstraction means showing only necessary details
# and hiding complex logic from the user.

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# User interacts only with simple methods, not internal logic
car = Car()
car.start_engine()
car.stop_engine()

print("\n---------------------------------------")

# -------------------------------
# 3️⃣ INHERITANCE
# -------------------------------
# Inheritance allows one class to use properties and methods of another.

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

# Student class inherits Person
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)     # Call parent constructor
        self.student_id = student_id

    def display(self):
        print(f"Student ID: {self.student_id}")

# Creating object of child class
student1 = Student("Ali", "ST123")
student1.show()
student1.display()

print("\n---------------------------------------")

# -------------------------------
# 4️⃣ POLYMORPHISM
# -------------------------------
# Polymorphism means "many forms" — different classes
# can have methods with the same name but different behaviors.

class Bird:
    def make_sound(self):
        print("Chirp Chirp")

class Dog:
    def make_sound(self):
        print("Bark Bark")

class Cat:
    def make_sound(self):
        print("Meow Meow")

# Using same method name but different behaviors
for animal in [Bird(), Dog(), Cat()]:
    animal.make_sound()

print("\n---------------------------------------")

# ✅ SUMMARY:
# 1. Encapsulation → Hiding data using private variables and methods
# 2. Abstraction → Hiding complex implementation using abstract classes
# 3. Inheritance → Reusing code from parent classes
# 4. Polymorphism → Same method behaving differently in different classes

print("All four OOP pillars demonstrated successfully!")
