dream_place = {}
active = True
while active:
    y_n = input("Would you like to respond? (y/n): ")
    if y_n == "y":
        name = input("Enter your name: ")
        place = input("If you could visit one place in the world,where would you go?")
        dream_place[name] = place
    else:
        active = False
print(dream_place)