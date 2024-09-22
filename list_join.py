list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 =[1.0,1.1,1.2]

list4 = list1 + list3

for x in list2:

  list1.append(x)
  
list2.extend(list1)
#print all join

print(list4)
print(list1)
print(list2)

