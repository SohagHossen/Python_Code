set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"sohag", "saimum"}
set4 = {"apple", "bananas", "cherry"}
#join all set  using |
myset = set1 | set2 | set3 |set4
#join all set  using union
myset1 = set1.union(set2, set3, set4)
print(myset)
print(myset1)