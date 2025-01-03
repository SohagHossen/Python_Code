import re



txt = "The rain in Banglasedh"
x = re.search("^The.*Bangladesh$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
