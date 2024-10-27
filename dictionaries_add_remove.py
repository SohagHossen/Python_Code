thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print single item using key
thisdict["year"] = 2018
print(thisdict)
# add new item 
thisdict["color"] = "red"
print(thisdict)
# add new item using update
thisdict.update({"price": "$22222"})
print(thisdict)
# remove item using del | pop | popitem 
del thisdict["model"]
print(thisdict)