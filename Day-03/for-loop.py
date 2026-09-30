for x in "kiwi":  # iteration through string
    print(x)
for x in "cat":
    print(x)
    if x == "a":
        break  # breaking loop after printing a
for x in "dog":
    if x == "o":
        break  # breaking loop before printing
    print(x)
for x in "bat":
    if x == "a":
        continue  # skipping
    print(x)
for x in range(3):  # from 0 to 2
    print(x)
for x in range(2, 5):  # from 2 to 4
    print(x)
for x in range(2, 10, 2):  # from 2 to 9 but increment 2 with each step
    print(x)
else:
    print("Done")  # executes when iteration in for is done
# nested loop
for x in "cat":
    for y in "dog":
        print(x, y)
# for loop cannot be empty.It at least needs a pass statement to execute
for x in range(100):
    pass
