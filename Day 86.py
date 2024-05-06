# 1 example 
# print(a:=False)

# 2 example 
numbers = [1, 2, 3, 4, 5]
while(n := len(numbers)) > 0:
    print(numbers.pop())

# 3 example 
happy = True
print(happy)

print(happy := True)

foods = list()
while (food := input("what food do you like?: ")) != "quit":
    foods.append(food)