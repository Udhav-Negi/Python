# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     line = f.readline()
#     i += 1
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student {i} in maths is: {m1}")
#     print(f"marks of student {i} in english is: {m2}")
#     print(f"marks of student {i} in SST is: {m3}")
#     print(line)
#     print(line, type(line))

f = open('myfile2.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()