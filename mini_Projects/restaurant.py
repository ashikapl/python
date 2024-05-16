menu = {'pizza':100,
        'burger':50,
        'dabeli':40,
        'franch fries':20,
        'hot dog':60,
        'manchurian':150
        }

print("Welcome, to our Restaurant!")
print("1. Pizza : Rs.100\n2. Burger : Rs.50\n3. Dabeli : Rs.40\n4. Franch Fries : Rs.20\n"
      "5. Hot Dog : Rs.60\n6. Manchurain : Rs.150\n")

order_money = 0

order_1 = input("Enter the first item you want to order: ")

if order_1 in menu:
    order_money +=  menu[order_1] # here is the total money of the item he/she ordered
    print(f"Your first order {order_1} has been added!") 
    
    order_2 = input("Do you want to add more items? (Yes/No)")

    if order_2.lower() == "yes":

        order_2 = input("Enter the second item you want to add: ")

        if order_2 in menu:
                order_money += menu[order_2]
                print(f"Your second order {order_2} has been added!")

        else:
              print(f"This {order_2} is not available yet!") 
else:
    print(f"This {order_1} is not available yet!")          

print(f"The total amount of items you to pay is:- {order_money}")

print("Thank You, for using our Website!")
           

