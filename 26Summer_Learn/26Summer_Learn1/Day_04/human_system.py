class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def print_info(self):
        print("Employee name: ", self.name)
        print("Employee id: ", self.id)
class Full(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    def calculate_monthly_salary(self):
        return None
class PartTime(Employee):
    def __init__(self, name, id, daily_salary):
        super().__init__(name, id)
        self.daily_salary = daily_salary
    def calculate_monthly_salary(self):
        return None