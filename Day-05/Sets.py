# sets are unordered and unchangeable
set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "banana", "cherry", "apple"}  # sets doesnt allow duplicates
print(set2)
# True and 1 and False and 0 are considered same
# can contain different type of data types in a set
# can count items in set using len()
set3 = set(("mango", "orange", "kiwi"))  # set constructor
print(set3)
# sets are unordered so cannot access by index
# to access set items use for loop
# adding items to set
# append adds item to last but sets are unordered so we use add
set1.add("orange")
print(set1)
list1 = ["kiwi", "mango"]
set1.update(set3)
print(set1)
set2.update(list1)  # doesnt need to be a set can be any iterable
# removing items
set2.remove("kiwi")
print(set2)
# set2.remove("kiwi") will raise Error if item not in this set
set2.discard("mango")  # this will not raise an error if item not in set
print(set2)
set2.pop()  # will remove any item
print(set2)
del set2  # entirely delete the set
# joining two sets
set2 = set((10, 20, 30))
set4 = set3.union(set2)  # join two sets
print(set4)
set = set1.union(set2, set3, set4)  # can be used to join multiple set
print(set)
# set= set1|set2|set3|set4 -same as union
setA = {"a", "b", "c"}
setB = {"a", "c", "e"}
setC = setA.intersection(setB)  # set with common elements
print(setC)
# can be also written as setC=setA & setB
setA.intersection_update(setB)  # this will change the original set
print(setA)
setD = setB.difference(setA)  # return items in setB which are not in setA
print(setD)
# can also be written as setD=setB-setA
# difference update () will change the original set
# return values not present in either set
setE = setB.symmetric_difference(setA)
print(setE)
# can also be written as setE=setB^setA
# symmetric_difference_update() will change the original set
# frozenset cannot be altered
setF = frozenset({15, 30, 45, 60})
print(setF)
