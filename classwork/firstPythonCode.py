### Printing hello world
print("Hello world!")

### Multipliying to numbers and fstring
x = 10
y = 5
print(f"The multiplication result of {x} and {y} is {x*y}")

### Taking input from the user
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

### User input for numbers
# try:
#     user_input = int(input("Enter a number between 1 to 10: "))
#     print(user_input*10)
# except ValueError:
#     print("Invalid value entered!")
# Arithmetic Error, ZeroDevisionError

# If condition example
### Write a code that checks the grade and returns the literal translation of the grade
grade = 63
def get_literal_grade(grade):
    if grade > 85:
        literal_grade = "A"
    elif grade > 75:
        literal_grade = "B"
    elif grade > 67:
        literal_grade = "C"
    elif grade > 60:
        literal_grade = "D"
    else:
        literal_grade = "F"
    return literal_grade
var1 = 76
print(f"You got {var1} which is equivalent to {get_literal_grade(var1)}")

# Create a function that takes as an input the radius of the circle and returns the area of the circle
import math
def get_area(r):
    return (math.pi * float(r)**2)

r = input("Enter circle radius: ")
print (f"For the radius of {r} the area of the circle is {round(get_area(r),2)}")
print (f"For the radius of {r} the area of the circle is {format(get_area(r), '.2f')}")
print (f"For the radius of {r} the area of the circle is {'{:.2f}'.format(get_area(r))}")
