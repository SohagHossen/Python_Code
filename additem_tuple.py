x = ("apple", "banana", "cherry")
#add single item inside tuple
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#add single item inside tuple
thislist = list(x)
thislist.append("orange")
print(thislist)
#remove single item inside tuple
thislist.remove("apple")
finaltuple = tuple(thislist)
print(finaltuple)

#we can delete tuple like this 
# del finaltuple