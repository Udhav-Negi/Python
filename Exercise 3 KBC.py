list = [["What is the capital of India", "Delhi", "Kolkata", "Chennai", "Dehradun", 1], ["Which is the largest ocean in the world", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", "Atlantic Ocean", 2]]

sum = 0
for item in list:
    print(item[0])
    print("1" + " " + item[1])
    print("2" + " " + item[2])
    print("3" + " " + item[3])
    print("4" + " " + item[4])
    x = int(input("Enter your answer 1, 2, 3, or 4?"))
    if(x == item[5]):
        print("Congratulations Correct Answer !")
        sum = sum + 100
    else:
        print("Wrong Answer")

print("Your total score is", sum)
