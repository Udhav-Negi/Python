# password generator logic created by me 
# import string, random
# if __name__ == "__main__":
#     # s1 = string.ascii_letters
#     s1 = string.ascii_lowercase
#     s1list = list(s1)
#     s2 = string.ascii_uppercase
#     s2List = list(s2)
#     s3 = string.digits
#     s3List = list(s3)
#     s4 = string.punctuation
#     s4List = list(s4)

#     # To do : Out of the different combination of s1, s2, s3 and s4 we have to create a password 

#     print(random.choice(s1list) + random.choice(s2List) + random.choice(s3List) + random.choice(s4List))


# Password generator logic created by cwh
import string, random
if __name__ == "__main__":
    # s1 = string.ascii_letters
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # To do : Out of the different combination of s1, s2, s3 and s4 we have to create a password 

    plen = input("Enter password length\n") #Todo1: Handle Gibberish
    # Handling Gibbersish 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    if len(plen) == 1 and (plen[0] == '0' or plen[0] == '1' or plen[0] == '2' or plen[0] == '3' or plen[0] == '4' or plen[0] == '5' or plen[0] == '6' or plen[0] == '7' or plen[0] == '8' or plen[0] == '9' ):
        print("Your password is: ")
        print("".join(random.sample(s, int(plen))))
    elif len(plen) == 2 and (plen[0] == '0' or plen[0] == '1' or plen[0] == '2' or plen[0] == '3' or plen[0] == '4' or plen[0] == '5' or plen[0] == '6' or plen[0] == '7' or plen[0] == '8' or plen[0] == '9' ) and (plen[1] == '0' or plen[1] == '1' or plen[1] == '2' or plen[1] == '3' or plen[1] == '4' or plen[1] == '5' or plen[1] == '6' or plen[1] == '7' or plen[1] == '8' or plen[1] == '9' ):
        # print(s)
        # random.shuffle(s)
        # print(s)
        print("Your password is: ")
        print("".join(random.sample(s, int(plen))))
        # print("".join(s[0:plen]))

    else :
        print("Please enter valid input !")
        

