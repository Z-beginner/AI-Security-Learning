class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes =2
class Humman(Mammal):
    def __init__(self, name, sex):
        super().__init__(name ,sex)
        self.has_tail = False
    def read(self):
        print(self.name, self.sex, self.num_eyes, self.has_tail)
class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True
    def read(self):
        print(self.name, self.sex, self.num_eyes, self.has_tail)
human = Humman("Human", 1)
cat = Cat("Cat", 0)
human.read()
cat.read()