tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

if 3421 in tup:
    print("Yes 342 is present in this tuple")

tup2 = tup[1 : 4]
print(tup2)