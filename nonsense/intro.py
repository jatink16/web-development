# Introduction to Python Concepts

# Greeting the user
print("Welcome to Python Programming!")
print("In this script, we'll explore a few basic concepts of Python.")

# Variables and data types
name = "Alice"
age = 25
height = 5.7

print(f"\nMeet {name}. She is {age} years old and {height} feet tall.")

# Lists and iteration
fruits = ["apple", "banana", "cherry"]
print("\nLet's explore a list of fruits:")
for fruit in fruits:
    print(fruit)

# Functions
def greet_user(username):
    return f"Hello, {username}! Welcome to Python."

greeting = greet_user("Bob")
print(f"\n{greeting}")

# Conditional Statements
num = 10
if num > 5:
    print("\nThe number is greater than 5!")
else:
    print("\nThe number is less than or equal to 5.")

# Loops
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Conclusion
print("\nThat's a quick introduction to some fundamental Python concepts!")
print("Python is a powerful and versatile programming language, and these are just a few examples of what you can do with it.")
