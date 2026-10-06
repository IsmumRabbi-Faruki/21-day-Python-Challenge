# tuples are ordered and unchangeable
tuple1 = ("banana", "cherry", "apple")
print(tuple1)
tuple2 = "mango", "apple"  # tuple can also be created without brackets
print(tuple2)
# tuples are ordered and accessed same as list using index and ranged index
# tuples allow duplicates
# tuple item can be counted using len function
# tuples can be empty
# tuples can contain different types of data type
tuple3 = tuple((12, 34, 45))  # tuple contructor
print(tuple3)
if "banana" in tuple1:  # checking item in tuple
    print("Yes")
# as tuples are unchangeable so tuples need to be converted to list for modification
list1 = list(tuple1)
print(list1)
list1[1] = "mango"
tuple_updated = tuple(list1)
print(tuple_updated)
# adding items
list2 = list(tuple2)  # using list and append
list2.append("cherry")
tuple2 = tuple(list2)
print(tuple2)
tuple4 = ("orange",)  # for single item tuple there must be a , after the item
tuple2 += tuple4  # using tuple+tuple
print(tuple2)
# for removing use list and remove()
# del works as same as for list
# unpacking a tuple
(red, green, yellow) = tuple3  # items of tuple3 gets assigned to variables
print(red)
# items cannot be samller than the number of variables
# items number can be greater in that case the last variable should be written with* to collect the remaining items
(one, *two) = tuple_updated
print(one)
print(two)  # returns a list
# tuples can also be looped like a list using for or range-len or while-len
# tuple items can be multiplied
tuple5 = tuple_updated*2
print(tuple5)
print(tuple5.count("banana"))  # count how many times the item has occured
print(tuple2.index("apple"))  # finds the first index item was found
