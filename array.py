cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

print("Append new item in array")
cars.append("Honda")
for x in cars:
  print(x)
  
print("Remove a item in array")
cars.pop(0)

print(cars)
