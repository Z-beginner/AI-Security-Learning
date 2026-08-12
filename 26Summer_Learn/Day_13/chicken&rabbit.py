def enter(name):
    number = input(f"enter the number of {name}:")
    nums = checker(number, name)
    return nums

def checker(number, name):
    try:
        number = int(number)
    except:
        return enter(name)
    else:
        if number <= 0:
            return enter(name)
        else:
            return number

def delicate(heads, feet):
    chickens_num = []
    for x in range(0,heads+1):
        if (heads-x)*4 == feet-x*2:
            chickens_num.append(x)
    return chickens_num

num1 = enter("heads")
num2 = enter("feet")
chickens = delicate(num1, num2)

if chickens:
    for chickens_num in chickens:
        rabbits_num = num1 - chickens_num
        print(f"chickens: {chickens_num}, rabbits: {rabbits_num}")
else:
    print("no answer")