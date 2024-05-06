dict = {}
with open("currency data.txt", "r") as f:
    contents = f.readlines()
    for content in contents:
        arr = content.split("\t")
        dict[arr[0]] = arr[1]


currency = input("Enter the currency you want to convert : ")
amount = int(input("Enter the amount you want to convert : "))

if(dict.get(currency)):
    print("amount is ", amount * float(dict.get(currency)))
else:
    print("Please enter valid currency")


# Practice for python array in split and join
# str = "udhav negi"
# arr = str.split(" ")
# print(arr)
# print(" ".join(arr))