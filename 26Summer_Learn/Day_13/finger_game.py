from random import randint

def enter():
    choice = input("只能选择石头，剪刀，布：")
    return checker(choice)

def checker(choice):
    dic = {
        "石头":0,
        "剪刀":1,
        "布":2
    }
    if choice in dic:
        return dic[choice]
    else:
        return enter()

def compare(num1,num2):
    if num1 - num2 == 1 or num2 - num1 == 2:
        print("你赢啦")
    elif num1 == num2:
        print("平局")
    else:
        print("你输啦")

random_number = randint(0,2)
choice_number = checker(input("请给出你的选择（石头，剪刀，布）："))
compare(random_number,choice_number)