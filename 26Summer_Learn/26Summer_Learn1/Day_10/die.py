from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
for i in range(1,11):
    m = Die()
    print(m.roll_die())