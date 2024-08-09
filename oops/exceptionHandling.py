# check for exception handling in python using try, except and finally keywords in python
# Since there are so many types of exception in python for this we can use (Exception keyword)

try:
    print("I want to run my code, if there is any exception then this try keyword print statement can't print on output")

except Exception as e: # here Exception is the keyword that provide any type of exception error
    print("Error comes, If there is any problem in this above try statement then this except statement will print on the output")
    
else:
    print("if no exception or error then else will print, If any chance this except statement not print or any error or problem then this else case will print")    
    
finally:
    print("This statement will print in all cases if the error comes or any problem will come or no error in every case this finally statement will print in any how")
    
    
    
# There are some exceptions for example

# ZeroDivisionError:->  Raised when division or modulo by zero takes place.
# ValueError:->  Raised when a function gets an argument of the right type but inappropriate value.
# TypeError:->  Raised when an operation or function is applied to an object of inappropriate type.
# FileNotFoundError:->  Raised when a file operation (like open) fails because the file doesn't exist.
# IndexError:->  Raised when trying to access an element from a list using an index that is out of range.
# etc..