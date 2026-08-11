from random import randint

def dif_choose():
    while True:
        try:
            difficulty_level = int(input("Please choose a difficulty\n(1:easy,2:medium,3:hard):\n"))
            if difficulty_level in [1,2,3]:
                return difficulty_level
            else:
                print("Please choose a number between 1 and 3:")
        except:
            print("Please enter a number:")

def game_preparation():
    difficulty = {
        "1": 100,
        "2": 1000,
        "3": 10000
    }
    level = dif_choose()
    max_num = difficulty[str(level)]
    correct_number = randint(1, max_num)
    return max_num, correct_number

def number_check(max_num, min_num):
    while True:
        try:
            number = int(input("Please enter a number:"))
            if number in range(min_num, max_num+1):
                return number
            else:
                print(f"Please choose a number between {min_num} and {max_num}:")
        except:
            print("Please enter a number:")

def guess():
    min_num = 1
    max_num, correct_number = game_preparation()
    correct = False
    while not correct:
        prompt = number_check(max_num, min_num)
        if prompt > correct_number:
            print("too big")
            max_num = prompt
        elif prompt < correct_number:
            print("too small")
            min_num = prompt
        else:
            print('you win')
            correct = True

def begin():
    print("Welcome to Guess Number")
    ready = input("Are you ready to begin?(y/n)")
    if ready == "y":
        guess()
    else:
        begin()

begin()