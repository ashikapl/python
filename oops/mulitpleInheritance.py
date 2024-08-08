# Multiple Inheritance from two base class(parent class) to one child class(derived class)

# parent or base class
class Father:
    def coder(self):
        print("I love coding")
    
    def skills(self):
        print("coding, programming")
    
# parent or base class
class Mother:
    def chef(self):
        print("I love cooking")
        
    def skills(self):
        print("art, cooking, reading books")
    
# child or derived class
class Child(Father, Mother):
    def student(self):
        print("I love studing")
        
    def skills(self):
        Father.skills(self) # here we can also call this base calls function methods 
        Mother.skills(self)
        print("Studing, learning new thing")
        
        
# object (instance of child class)       
c = Child()
c.coder()
c.chef()
c.student()
c.skills()