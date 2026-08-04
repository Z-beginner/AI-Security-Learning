#range
print(list(range(1,10)))
print(list(range(1,10,2)))
print(sum(range(1,10)))

#squares
squares = []
for i in range(1,10):
    squares.append(i**2)
print(squares)
# **2

#列表推导式
squares1 = [x**2 for x in range(1,10)]
print(squares1)

lifang_xiao = [y**3 for y in range(1,10)]
print(lifang_xiao)