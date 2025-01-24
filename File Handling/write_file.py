f = open("student.txt", "a")
f.write("Add new conten in this file")
f.close()


f = open("student.txt", "r")
print(f.read())