# pyramid design
for x in range(4):
    for y in range(4-x-1):
        print(" ", end="")
    for z in range(2*x+1):
        print("*", end="")
    print()
# multiplication table
for x in range(10):
    print(5*(x+1))  # proper table will be learnt after f string
# FizzBuzz
for x in range(30):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print(x)
