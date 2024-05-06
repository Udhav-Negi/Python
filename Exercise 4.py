str = input("Enter any word to decode ")

# encoding
if(len(str) >= 3):
    ch = str[0]
    str = str[1:]
    str = str + ch

    str = "abc" + str + "xyz"
else:
    str = str[::-1]

print(f"encoded string is {str}")
# decoding 
if(len(str) < 3):
    str = str[::-1]
else:
    if len(str) == 3:
        str = ""
    else:
        str = str[3:]
        str = str[:len(str)-3]
        ch = str[len(str)-1]
        str = str[:len(str)-1]
        str = ch + str
print(f"ans is {str}")