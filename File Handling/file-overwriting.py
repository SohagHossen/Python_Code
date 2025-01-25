f = open("student.txt", "w")
f.write("Woops! I have deleted your content!")
f.close()

f = open("student.txt", "r")
print(f.read())