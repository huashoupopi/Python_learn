class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.step=0
    def get_name(self):
        long_name="This is my "+str(self.year)+" "+self.make+" "+self.model
        print(long_name.title())
    def read_step(self):
        print("It has "+str(self.step)+" on it!")
    def update(self,mileage):
        if mileage>self.step:
            self.step=mileage
        else:
            print("it can't roll back!")
    def add_step(self,miles):
        self.step+=miles

my_car =Car("aodi","a6",2016)
my_car.get_name()
my_car.read_step()
my_car.update(500)
my_car.update(400)
my_car.read_step()
my_car.add_step(20)
my_car.read_step()
#继承
class Buttery:
    def __init__(self,butter):
        self.butter=butter
    def get_bu(self):
        print("目前电量百分百")
class ElectricCar(Car,Buttery):
    def __init__(self,make,model,year,butter):
        Car.__init__(self,make,model,year)
        Buttery.__init__(self,butter)
My_telsa=ElectricCar("telsa","model_s",2022,70)
My_telsa.get_name()
