
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.odl = 10

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
            
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} -KWh battery")

my_tesla = ElectricCar("tesla","model s",2016,"45%")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
