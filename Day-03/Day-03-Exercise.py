# FOR_LOOP_EXERCISE
# Create a list called fruits with: "apple", "banana", "cherry"
# Write a for loop that prints each item in fruits
# Use break to stop the loop when the item is "banana"
list1 = ["apple", "banana", "cherry"]
for x in list1:
    if x == "banana":
        break
    print(x)
# WHILE_LOOP_EXERCISE
# Create a variable i with the value 0
# Write a while loop that runs as long as i is less than 6
# Inside the loop: increment i by 1
# If i equals 3, use continue to skip that iteration
# Print i
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# PYRAMID_DESIGN
for x in range(4):
    for y in range(4-x-1):
        print(" ", end="")
    for z in range(2*x+1):
        print("*", end="")
    print()
# MULTIPLICATION_TABLE
for x in range(10):
    print(5*(x+1))  # proper table will be learnt after f string
# FIZZBUZZ
for x in range(30):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print(x)
