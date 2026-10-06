# lists are ordered and changeable
list1 = ["apple", "banana", "cherry"]
print(list1)
print(list1[1])  # lists are indexed
# allow duplicate members as they are indexed
list2 = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(list2))  # len function on list
print(type(list2))
# list can contain different types of data types
list3 = ["abc", 34, True, "Donald_Trump", False]
list4 = list(("apple", "banana", 34))  # list constructor ( double brackets)
print(list4)
# list follow indexing rules as strings
print(list1[1:2])
print(list2[2:])
print(list3[-3:-1])
# checking items in list
if 34 in list3:
    print("Yes")
# modyfying list items
list1[1] = "kiwi"  # changing list items
print(list1)
list2[1:3] = ["kiwi", "jackfruit"]  # changing a range of items
print(list2)
# range is more than items replaced len is decreased
list3[0:2] = ["Barack_Obama"]
print(list3)
list4[1:2] = ["apple", "banana"]  # len is increased
print(list4)
# insert without replacing
list4.insert(1, "kiwi")  # index, item
print(list4)
# add items to the last
list4.append("mango")
print(list4)
# to append another list to a list
list4.extend(list2)
print(list4)
# removing items
list4.remove(34)  # removes the item
print(list4)
list4.remove("apple")  # if multiple same items ,removes the first one
print(list4)
list4.pop(1)  # removes specified index
print(list4)
list4.pop()  # if not specified it removes the last item
print(list4)
del list4[4]  # removes specified index
print(list4)
del list1  # deletes entire list
# print(list1) will return error
list2.clear()  # clears the list
print(list2)
# looping through lists
for x in list3:
    print(x)
for i in range(len(list3)):  # using range and len
    print(list3[i])
j = 0
while j < len(list3):  # using while and len
    print(list3[j])
    j += 1
# list comprehension
list2 = ["True" for x in list3 if x != False]
print(list2)
# sorting the list
list4.sort()  # sorts alphanumerically #capital letters will get sorted before lowercase
print(list4)
list4.sort(reverse=True)
print(list4)
list4.sort(key=str.lower)  # case insensitive sort
print(list4)
list4.reverse()
print(list4)
# copying lists #if we write list1=list2 then list1 is a reference to list2 then if we change list2 list1 will also change so thats why we need copy
list1 = list3.copy()
print(list1)
list5 = list(list1)
print(list5)
# joining lists
listA = list2+list3  # using +
print(listA)
for x in list2:  # using loop and append
    list3.append(x)
print(list3)
