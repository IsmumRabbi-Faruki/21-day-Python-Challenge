x = 15
y = 4
# 1.Arithmetic Operators (+,-,/,*,//,**,%)
print(x+y)
# 1.1 use of / & // [/ returns float,// retruns int]
print(x/y)
print(x//y)
# 1.2 ** is used as power
print(y**2)
print(y*2)
# 1.3 % is used for remainder
print(x % y)
# 2.Assignment Operators (+=,-=,*=.....)
x += 4
print(x)
x -= 4
print(x)
# 3.Comparison Operator(==,>=,<=,>,<,!=)
print(x == y)  # will return a bool value
print(y != 4)
# 3.1 We can do range comparisons
print(0 < y < 3)
print(10 < x <= 15)
# 4.Logical Operators ( and, or , not)
print(x > 10 and x < 20)  # returns True is both of them are true
print(x > 10 or x > 20)  # returns True is either one of them is true
print(not (10 < x < 20))  # reverses the initial returned value
# 5.Identity Operator (is,is not)
z = x
print(z is x)
# 5.1 is and == are not same
a = 10
b = 10
print(a == b)
print(a is b)


# CHECK PYTHON OPERATORS PRECEDENCE
