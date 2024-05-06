# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)
# average(4, 6)
# average(b=9)

# average(b=9, a=21)
c = average(5, 6, 7, 1)
print(c)

def name(**name):
    print(type(name))
    print("hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")