
try:
    a = int(input("Enter the number: "))
    print(f"Multiplication table of {a} is:")
    for i in range(1, 11):
        print(f"{a} X {i} = {a*i}")

# except Exception as e:
except ValueError:
    print("Invalid Input")
print("Some important lines of code")
print("End of Program")