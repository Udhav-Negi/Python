# Write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard

sum = 0
while True:
    print("Press q to quit")
    x = input("Enter the price of the item: ")
    match x:
        case 'q':
            break
        case _ if int(x) > 0:
            sum = sum + int(x)
        case _:
            print("Please enter valid price")

print(f"sum is {sum}")