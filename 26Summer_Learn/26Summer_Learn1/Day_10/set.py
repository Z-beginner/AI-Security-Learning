#突然发现前面没有学习集合
set1 = set()
#创建集合需要用set()，而不能直接{}
set2 = {"a", "b", "c", "d", "e", "f"}
set3 = {"a", "b", "c", "x", "y", "m"}
set3.add("z")
set3.remove("m")
print("z" in set3)

set4 = set3 & set2
print(set4)
#交集

set5 = set3 | set2
print(set5)
#并集

set6 = set3 - set2
print(set6)
set7 = set2 - set3
print(set7)
#差集