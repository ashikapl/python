# A simple calculator which perfoms addition, subtraction, multiplication, and division

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Can't divide by zero."
    else:
        return a / b   

choice = int(input("Select the option you want to do:\n1.Add\n2.subtraction\n3.Multiplication\n4.Division\n"))

if choice not in [1,2,3,4]:
    print("Please Enter the valid option..!")

else:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print(addition(a,b))
        
    elif choice == 2:
        print(subtraction(a,b))
        
    elif choice == 3:
        print(multiplication(a,b))
        
    elif choice == 4:
        print(division(a,b))   
        
    else:
        print("Please Enter the valid number...!")