# Strings are arrays
a = "My name is Hecker"
print(a[3])
for x in a:  # looping through string
    print(x, end="")
print(len(a))  # length of string
print("name" in a)  # ReturnsBool
# slicing string
print(a[2:5])  # starts from 2 and ends before 5
print(a[:7])  # starts from beginning
print(a[1:])  # slices till the end
print(a[-7:-2])  # negative indexing
# string modification
print(a.upper())  # uppercase conversion
print(a.lower())  # lowercase conversion
print(a.strip())  # removes whitespace from beginning or end
print(a.replace("n", "f"))  # replaces this with that
# splits string from this,doesnt include it anymore, two parts stored in a list
print(a.split("s"))
# joining two strings
x = "Hecker"
y = "Boy"
z = x+y  # Strings are joined
print(z)
z = x+" "+y  # addition of space
print(z)
# adding strings and numbers
age = 24
c = f"Hello! My name is Hecker. I am {age} years old "
print(c)
# we can directly write f string in print and do calculation inside placeholder
print(f"Hello! my fav num is {20*31}")
# escape characters
print("\"Messi\" is the GOAT")  # Double quotes inside double quotes
print("\'Messi\' is the GOAT")  # single quotes
print("Messi is the \nGOAT")  # newline
