# dictionaries hold key and value pair
# dictionaries are ordered and changeable but doesnt allow duplicates
dict1 = {"name": "Jack", "age": 22, "sex": "Male"}
print(dict1)
# cannot have same two keys
print(len(dict1))
# dictionaries can also contain lists as values
dict2 = dict(name="John", age=24, citizenship="Valid")  # dict contructor
print(dict2)
# acessing items
print(dict1["name"])  # gets values for keys
print(dict1.get("name"))  # another way
print(dict1.keys())  # returns a list of all keys
print(dict1.values())  # returns a list of all values
print(dict1.items())  # returns a list of key value pairs
# changing values
dict1["age"] = 23  # directly accessing key
print(dict1)
dict2.update({"age": 22})  # using update
print(dict2)
# adding values
# methods for changing keys also apply here but the key has to a new one
dict1["height"] = "6ft"
dict2.update({"height": "6ft"})
print(dict1)
print(dict2)
# removing items
dict2.pop("citizenship")
print(dict2)
del dict1["sex"]
print(dict1)
# clear clears the dictionary whereas del can delete the whole dictionary
# looping through dictionary
for x in dict1:  # loops through the keys
    print(x)
for x in dict1.values():  # loops through values
    print(x)
for x in dict2:
    print(dict2[x])  # also loops through values
for x, y in dict2.items():  # loops through keys and values
    print(x, y)
# copying dictionary
dict3 = dict2.copy()
print(dict3)
dict4 = dict(dict1)
print(dict4)
# nested dictionary
family = {"mother": {"name": "Sabrina", "age": 36},
          "father": {"name": "Jonathan", "age": 40},
          "child1": {"name": "David", "age": 15},
          "child2": {"name": "Emily", "age": 12}}
print(family["child1"]["age"])  # accessing nested dictionary items
# looping through nested dict
for x, y in family.items():
    print(f"{x}:", end="")
    for z in y:
        print(f"{y[z]}", end="")
