thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("print dict using for loop")
for x in thisdict:
  print(thisdict[x])

print("print dict all value using for loop")
for x in thisdict.values():
  print(x)
print("print dict all keys using for loop")
for x in thisdict.keys():
  print(x)

print("print dict all  iteam using for loop")
for x, y in thisdict.items():
  print(x, y)