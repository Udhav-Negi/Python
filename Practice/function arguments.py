def fun(*name):
    # print('type is ', type(name))
    print("printing")
    for item in name:
        print(item)

def fun1(**name):
    print('type is ', type(name))
    print(name)
    

fun1(item1 = "item1", item2 = "item2", item3 = "item3")
# fun("item1", "item2", "item3")