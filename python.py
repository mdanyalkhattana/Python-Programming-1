# ------------------------------------------------------------
# PYTHON FULL BASICS - STUDY GUIDE
# Author: Muhammad Danyal
# Purpose: To understand all basic Python concepts with examples
# ------------------------------------------------------------

# -----------------------
# 1. PRINT STATEMENT
# -----------------------
print("Welcome to Python Programming!")  # Output text to console

# -----------------------
# 2. VARIABLES AND DATA TYPES
# -----------------------
name = "Danyal"     # String
age = 25            # Integer
height = 5.9        # Float
is_programmer = True # Boolean

print(name, age, height, is_programmer)

# -----------------------
# 3. DATA TYPE CHECKING
# -----------------------
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_programmer))  # <class 'bool'>

# -----------------------
# 4. INPUT FROM USER
# -----------------------
# user_name = input("Enter your name: ")
# print("Hello", user_name)

# -----------------------
# 5. OPERATORS
# -----------------------
x = 15
y = 4
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# -----------------------
# 6. COMPARISON & LOGICAL OPERATORS
# -----------------------
a, b = 10, 20
print(a > b)  # False
print(a == 10 and b == 20)  # True
print(a < 5 or b > 15)      # True
print(not(a == b))          # True

# -----------------------
# 7. IF - ELSE CONDITIONS
# -----------------------
if age >= 18:
    print("Adult")
elif age > 13:
    print("Teenager")
else:
    print("Child")

# -----------------------
# 8. LOOPS
# -----------------------

# FOR LOOP
for i in range(1, 6):
    print("Number:", i)

# WHILE LOOP
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# -----------------------
# 9. LISTS
# -----------------------
numbers = [10, 20, 30, 40]
print(numbers)
numbers.append(50)    # Add item
numbers.insert(1, 15) # Insert at index
numbers.remove(30)    # Remove item
print(numbers)
print(len(numbers))   # Length of list

# Loop through list
for n in numbers:
    print("Value:", n)

# -----------------------
# 10. TUPLES
# -----------------------
colors = ("red", "green", "blue")
print(colors[1])      # Access item
# Tuples are immutable (cannot change)

# -----------------------
# 11. SETS
# -----------------------
myset = {1, 2, 3, 3, 4}
print(myset)          # Duplicates removed automatically
myset.add(5)
myset.remove(2)
print(myset)

# -----------------------
# 12. DICTIONARIES
# -----------------------
student = {
    "name": "Ali",
    "age": 21,
    "course": "AI"
}
print(student)
print(student["name"])     # Access value
student["age"] = 22        # Update value
student["grade"] = "A"     # Add new key-value
print(student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# -----------------------
# 13. FUNCTIONS
# -----------------------
def greet(person="User"):
    """Function with default argument"""
    print(f"Hello, {person}!")

greet()
greet("Danyal")

def add(a, b):
    return a + b

result = add(5, 10)
print("Sum:", result)

# -----------------------
# 14. LAMBDA FUNCTION
# -----------------------
square = lambda n: n * n
print(square(5))

# -----------------------
# 15. LIST COMPREHENSION
# -----------------------
squares = [x**2 for x in range(1, 6)]
print(squares)

# -----------------------
# 16. STRING METHODS
# -----------------------
text = "python is powerful"
print(text.upper())       # Uppercase
print(text.title())       # Title case
print(text.replace("powerful", "awesome"))  # Replace words
print("powerful" in text) # Membership check

# -----------------------
# 17. FILE HANDLING
# -----------------------
with open("demo.txt", "w") as file:
    file.write("This is a demo file.\nPython is great!")

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# -----------------------
# 18. EXCEPTION HANDLING
# -----------------------
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("Try-except block executed.")

# -----------------------
# 19. MODULES AND IMPORTS
# -----------------------
import math
print(math.sqrt(25))
print(math.pi)

from datetime import datetime
print("Current Date & Time:", datetime.now())

# -----------------------
# 20. CLASSES AND OBJECTS
# -----------------------
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

car1 = Car("Toyota", "Red")
car1.show_info()

# -----------------------
# 21. INHERITANCE
# -----------------------
class ElectricCar(Car):
    def __init__(self, brand, color, battery_capacity):
        super().__init__(brand, color)
        self.battery = battery_capacity

    def show_details(self):
        print(f"{self.brand} | {self.color} | Battery: {self.battery} kWh")

tesla = ElectricCar("Tesla", "Black", 75)
tesla.show_details()

# -----------------------
# 22. POLYMORPHISM
# -----------------------
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

for animal in [Dog(), Cat(), Animal()]:
    animal.sound()

# -----------------------
# 23. ITERATORS
# -----------------------
mylist = [1, 2, 3]
iterator = iter(mylist)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# -----------------------
# 24. GENERATORS
# -----------------------
def generate_numbers():
    for i in range(3):
        yield i

for num in generate_numbers():
    print(num)

# -----------------------
# 25. DECORATORS
# -----------------------
def decorator_function(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator_function
def say_hello():
    print("Hello, decorated function!")

say_hello()

# -----------------------
# 26. ENUMERATE
# -----------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# -----------------------
# 27. ZIP FUNCTION
# -----------------------
names = ["Ali", "Sara", "John"]
scores = [85, 90, 88]
for name, score in zip(names, scores):
    print(name, ":", score)

# -----------------------
# 28. MAP, FILTER, REDUCE
# -----------------------
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squares:", squared)

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
print("Sum of numbers:", total)

# -----------------------
# 29. JSON HANDLING
# -----------------------
import json
person = {"name": "Ali", "age": 25, "city": "Lahore"}

# Convert to JSON string
json_str = json.dumps(person)
print(json_str)

# Convert back to dictionary
dict_data = json.loads(json_str)
print(dict_data["name"])

# -----------------------
# 30. END OF FILE
# -----------------------
print("✅ All Python basics covered successfully!")
