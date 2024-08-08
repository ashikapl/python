# Inheritance in oops how a base class is inherit from derived class (child is inherit from parent class)

# parent or base class
class Vehicle:
    def general_usage(self):
        print("General usage: For Transportation")
        
# child or derived class
class Car(Vehicle):
    def __init__(self):
        print("I'm a Car")
        self.wheels = 4
        self.has_roof = True
        
    def specific_usage(self):
        # self.general_usage() # we can call function of parent class also in child class or can call directly after creation of object  
        print("Vacation with family, or commute to work")
        
# other child or derived class
class Bike(Vehicle):
    def __init__(self):
        print("I'am a Bike")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        # self.general_usage() # we can call function of parent class also in child class or can call directly after creation of object  
        print("Road trip, or Racing")
        
# instance or object of class
c = Car()
# c.general_usage()
# c.specific_usage()
# print(c.wheels)
# print(c.has_roof)

# print(issubclass(Car,Vehicle)) # here we check the Car class is inherit(or child class) of Vehicle class(parent Classs)
print("Car is inherit from Bike class->" , issubclass(Car,Bike)) 

print(isinstance(c, Car)) # here we check that c is an object of an Car class or not it returns true or false

b = Bike()
# b.general_usage()
# b.specific_usage()
# print(c.wheels)
# print(c.has_roof)

print("b is an object of Bike class->" , isinstance(b, Bike))
print("Bike is inherit from vehicle class->" , issubclass(Bike, Vehicle))
