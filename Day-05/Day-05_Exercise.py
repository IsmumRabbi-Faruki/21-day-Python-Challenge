# TUPLE_EXERCISE:
# Create a tuple called fruits with the values "apple", "banana", "cherry"
# Print the second item in the tuple
# Print the number of items using len()
# Unpack the tuple into three variables a, b, c
# Print the variable b
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])
print(len(tuple1))
(a, b, c) = tuple1
print(b)
# SET_EXERCISE
# Create a set called colors with the values "red", "green", "blue"
# Print the set
# Add "yellow" to the set using add()
# Remove "green" from the set using discard()
# Print the number of items using len()
set1 = {"red", "green", "blue"}
print(set1)
set1.add("yellow")
set1.discard("green")
print(set1)
print(len(set1))
# DICTIONARY_EXERCISE
# Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# Print the value of the "model" key
# Add a new key "color" with the value "red"
# Remove the "brand" key using pop()
# Print the dictionary
dict1 = dict(brand="Ford", model="Mustang", year=2024)
print(dict1["model"])
dict1["color"] = "red"
dict1.pop("brand")
print(dict1)
# CONTACT_BOOK
contact = {}
while True:
    a = int(input("Press 1 for Adding Contact\nPress 2 to Search\nPress 3 to Delete\nPress 4 to View\nPress 5 to Exit\n"))
    if a == 1:
        name = input("Enter name:")
        number = input("Enter number")
        contact[name] = number
    elif a == 2:
        search = input("Enter name:")
        for x, y in contact.items():
            if x == search:
                print(x, y)
    elif a == 3:
        delete = input("Enter name:")
        contact.pop(delete)
        print("Success")
    elif a == 4:
        print(contact)
    else:
        break
