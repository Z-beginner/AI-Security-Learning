active = True
price = 0
while active:
    age = input("Enter your age: ")
    if age != "quit":
        age = int(age)
        if age < 3:
            continue
        elif age < 12:
            price += 10
        else:
            price += 15
    else:
        active = False
print("the total price is", price)

#break
#else:
#    break