thislist = ["apple", "banana", "cherry"]

print("Normal print using for looping")

for i in thislist:
	print(i)
print("\n")
print("Print using range and len")

for i in range(len(thislist)):
  print(thislist[i])

print("\n")

print("Print using while loop")
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1