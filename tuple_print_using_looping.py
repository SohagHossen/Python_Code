thistuple = ("apple", "banana", "cherry")
print("print normal looping")
for x in thistuple:
  print(x)
  
print("\n")
print("print using len funtion")
for i in range(len(thistuple)):
  print(thistuple[i])

print("\n")  
print("print using while funtion")

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1