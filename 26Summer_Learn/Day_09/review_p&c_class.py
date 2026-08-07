class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"{self.name} is {self.age} years old")
class Tanker(Car):
    def __init__(self, name, age, tank_cap):
        super().__init__(name, age)
        self.tank_cap = tank_cap
    def mileage(self):
        mileage = self.tank_cap * 5
        return mileage
class ElectricCar(Car):
    def __init__(self, name, age, electric_cap):
        super().__init__(name, age)
        self.electric_cap = electric_cap
    def mileage(self):
        mileage = self.electric_cap * 10
        return mileage


def real_mileage(mileage, way_kind="straight"):
        if way_kind == "straight":
            real_mileage = mileage
            return real_mileage
        elif way_kind == "uphill":
            real_mileage = mileage * 0.7
            return real_mileage
        elif way_kind == "downhill":
            real_mileage = mileage * 1.2
            return real_mileage


car1 = Tanker("car1", 10, 5)
car1_mileage = car1.mileage()
car1_real_mileage = real_mileage(car1_mileage)
car2 = ElectricCar("car2", 10, 7)
car2_mileage = car2.mileage()
car2_real_mileage = real_mileage(car2_mileage, "uphill")
print(car1_real_mileage)
car2.display()
print(car2_real_mileage)


#注意class中的def才需要使用self，不要搞混了！！！