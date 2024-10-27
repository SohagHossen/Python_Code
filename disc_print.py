thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("print all value")
for x in thisdict:
  print(x)

print("print single value ")
for x in thisdict:
  print(thisdict[x])

print("print all items using value ")

for x in thisdict.values():
  print(x)
print("print all items using keys")
for x in thisdict.keys():
 print(x)
 