#Unordered,Unchangeable,Duplicates Not Allowed

set1 = {"apple", "banana", "cherry", False, True, 0}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#print all value 
print(set1)
print(set2)
for x in set3:
  print(x)
#print length set2

print("The length is:",len(set2))


#add new value in set anslo using update(mylist)
print("print after new value added")
set2.add(4)
print(set2)

set2.remove(3)

#Note: If the item to remove does not exist, remove() will raise an error.
print("print after remove 3 = ",set2)
#Note: If the item to remove does not exist, discourt() will not raise an error.
set2.discard(3)
print(set2)

popitem=set1.pop()
print("The pop item is :",popitem)
print("print after pop value from set1:",set1)