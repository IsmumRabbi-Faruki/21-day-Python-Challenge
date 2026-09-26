x = 12
y = 0
if x > y:             # if condition : code to be executed
    print("Yes")
elif y < x:
    print("Whatever")  # elif same syntax #when if becomes false it goes to elif
else:
    print("Python")  # applies when all other if and elif are false
a = 2
b = 2
if a == b:
    print("Equal")  # doesnt always need a else statement to run, or elif
elif a != b:
    print("X")
a = 3
b = 5
if a < b:
    print("a")  # short hand if
print("a") if a < b else print("b")  # short hand if else #ternary operator
c = a if a < b else b  # assigning value to a variable using
print(c)
# logical operator and if-else
if (a == c) and (a == b):
    print("a=b=c")
if ((a > 0) or (b > 0)) and c > 0:  # multiple
    print("Test")
# nested if-else
age = 20
record = True
card = False
if age > 18:
    if record == False:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
# hybrid nesting with logical
if age > 18:
    if record == True and card == True:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    pass  # pass statement
