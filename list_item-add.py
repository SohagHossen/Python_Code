thislist = ["apple", "banana", "cherry"]
thislist.append("blackcurrant")
newlist = thislist.copy()
newlist[1:3] = ["jackfood", "watermelon"]
print(thislist)
print(newlist)