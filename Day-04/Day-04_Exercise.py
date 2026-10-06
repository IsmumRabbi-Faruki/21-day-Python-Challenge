# STRINGS_EXERCISE
# Create a variable txt with the value "Hello, World!"
# Print the characters from index 2 to 5 (slicing)
# Print txt converted to upper case
# Create a variable name with the value "Python"
# Use an f-string to print "I love Python" using the name variable
txt = "Hello,World!"
print(txt[2:6])
print(txt.upper())
name = "Python"
print(f"I love {name}")
# LISTS_EXERCISE
# Create a list called colors with the values "red", "green", "blue"
# Print the first item in the list
# Change the second item to "yellow"
# Add "purple" to the end of the list using append()
# Remove "red" from the list using remove()
# Print the list
list10 = ["red", "green", "blue"]
print(list10[0])
list10[1] = "yellow"
list10.append("purple")
list10.remove("red")
print(list10)
# PALINDROME_CHECKER
is_palindrome = True
word = input("Enter a word:")
n = len(word)
for i in range(n//2):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

# WORD_COUNTER
paragraph = input("Enter Text:")
for char in ".,!?":
    new_text = paragraph.replace(char, " ")
list1 = new_text.split()
print(len(list1))
