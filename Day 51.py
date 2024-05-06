with open('myfile.txt', 'r') as f:
    print(type(f))
    f.seek(10)
    data = f.read(5)
    print(data)