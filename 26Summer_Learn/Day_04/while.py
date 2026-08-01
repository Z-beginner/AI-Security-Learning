#输入n个数，来求取它们的平均值
numbers = []
times = 0
while not "stop" in numbers:
    times += 1
    enter = input("enter numbers: ")
    numbers.append(enter)
numbers.remove("stop")
add = 0
for number in numbers:
    add += int(number)
# 可以使用sum
average = add / times
print(average)