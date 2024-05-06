f = open("myfile.txt", 'rb')
# print(f)

text = f.read()
print(text)
f.close()

# Writing to a file
# f = open("myfile.txt", 'w')
f = open("myfile.txt", 'a')
f.write(' Hello world')
f.close()