# A basic of CLASSES and OBJECT

# Classes are blueprint of an object
# Abstract of an entity which has a common set of properties and methods

# Class (Class of Human)
class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
        
    def do_work(self):
        if self.occupation == "chef":
            print(self.name, "Cooks food")
        elif self.occupation == "actor":
            print(self.name, "Shoots the film")
            
    def speaks(self):
        print("Hey, I am", self.name)
        
        
# Object (instance of class)

nisha = Human("Nisha Madhulika", "chef")
nisha.do_work() 
nisha.speaks() 

salman = Human("Salman Khan", "actor")
salman.do_work()
salman.speaks()     
