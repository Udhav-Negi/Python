from functools import reduce
def cube(x):
    return x * x *x

print(cube(2))
newl = []

l = [1, 2, 3, 4, 5, 6]
# for item in l :
#     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)

# FILTER

def filter_function(a):
    return a > 4
newnewl = list(filter(filter_function, l))

print(newnewl)

sum = reduce(lambda x, y : x + y, l)
print(sum)