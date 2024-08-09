# Exception class
# an accident class of which occur when an exception comes

class Accident(Exception): # here Exception is base class of exceptions
    def __init__(self,msg):
        self.msg = msg
        
    def handle(self):
        print("Take another root to go!")
        
try:
    raise Accident("Tow cars are crashed!")

except Accident as a:
    a.handle()
    
finally:
    print("Go well!")
