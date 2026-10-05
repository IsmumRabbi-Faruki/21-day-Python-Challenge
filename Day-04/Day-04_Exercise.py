# palindrome Checker
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

# word counter
paragraph = input("Enter Text:")
for char in ".,!?":
    new_text = paragraph.replace(char, " ")
list1 = new_text.split()
print(len(list1))
