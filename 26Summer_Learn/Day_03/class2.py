class Dog:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print('我是',self.name)
dog1 = Dog("Tom")
dog1.introduce()

class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def introduce(self):
        print('我是',self.name)
        print('今年',self.age)
s1 = Student("Tom", 18)
s1.introduce()

class Phone:
    def __init__(self, brand , battery):
        self.brand = brand
        self.battery = battery
    def show_battery(self):
        print('当前电量：',self.battery)
    def use(self):
        self.battery = self.battery - 20
phone1 = Phone("Apple",100)
phone1.show_battery()
phone1.use()
phone1.show_battery()