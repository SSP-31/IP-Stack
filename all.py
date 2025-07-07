# Hello World
print("Hello,Welcome to Python World!")

# Variables and Data Types
name = "Shivani"
age = 21
height = 5.2
is_student = True

# Lists
fruits = ["Apple", "Banana", "Cherry","Mango"]
print(fruits[1])  # Access second item

# Tuples (Immutable)
coordinates = (10, 20)

# Dictionaries
student = {"name": "SSP", "age": 21, "grade": "A"}
print(student["name"])

# Conditional Statements
if age > 18:
    print("Adult")
else:
    print("Minor")

# Loops
# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Pythonista"))

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old.")

p = Person("SSP", 21)
p.introduce()

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# Importing Libraries
import math
print(math.sqrt(16))

# Exception Handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")




