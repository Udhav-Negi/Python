import os 
# f = os.open("myfile.txt", os.O_RDONLY)
# content = os.read(f, 10)
# print(content)

# print(os.listdir())
str = input("Write the type of file you want to rename: txt, pdf")

i = 2
if str == "txt" or str == "pdf":
    for file in os.listdir():
        if file.endswith(str):
            os.rename(file, f"{i}.pdf")
            i += 1