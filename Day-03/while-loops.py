i = 1
while i < 6:
    print(i)
    i += 1  # must add increment otherwise loop will run forever
j = 1
while j < 5:
    print(j)
    if j == 3:
        break  # use break to break loop
    j += 1
k = 1
while k < 3:
    k += 1
    if k == 2:
        continue  # skips current iteration and continues to next
    print(k)
l = 1
while l < 3:
    print(l)
    l += 1
else:
    print("Greater than 3")  # executes when while becomes false
