nums = []
compared =[]
while True:
    inputed = input("Enter a number:")
    if inputed == "stop":
        break
    else:
        nums.append(float(inputed))
while nums != []:
    num1 =max(nums)
    compared.append(num1)
    nums.remove(max(nums))
print(compared)
#昨天不知道有max和break，原来可以这么简单