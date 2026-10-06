# CONDITIONALS_EXERCISE
# Create a variable age with the value 20
# Write an if statement that prints "Child" if age is less than 13
# Add an elif that prints "Teenager" if age is less than 18
# Add an else that prints "Adult"
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
# OPERATOR_EXERCISE
# Create two variables a = 15 and b = 4
# Print the result of a modulus b (the % operator)
# Print the result of a floor division b (the // operator)
# Print the result of a to the power of b (the ** operator)
# Use an assignment operator to add 10 to a (use +=)
a = 15
b = 4
print(a % b)
print(a//b)
print(a**b)
a += 10
print(a)
# ODD_EVEN
a = int(input("Enter number:"))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")
# POSITIVE_NEGATIVE
if a == 0:
    print("Zero")
elif a > 0:
    print("Positive")
else:
    print("Negative")
