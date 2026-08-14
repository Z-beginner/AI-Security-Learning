class Phone:
    def __init__(self,brand,battery):
        self.brand = brand
        self.battery = battery
    def call(self, sb):
            self.sb = sb
            print("正在给", sb, "打电话")
    def show_battery(self):
            print("当前电量为：", self.battery)
phone1 = Phone("Apple",100)
phone1.call("Tom")
phone1.show_battery()