import json


x = '{ "name":"sohag", "age":37, "city":"Dhaka"}'


y = json.loads(x)


print(y["age"])
