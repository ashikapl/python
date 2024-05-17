# Task Management 
def task():
    tasks = [] # empty list
    print("----------WELCOME TO OUR TASK MANAGEMENT PROGRAM---------")
    
    total_task = int(input("Enter the number of tasks you want to do: "))
    
    for i in range(1,total_task+1):
        task_name = input(f"Enter the task {i}: ")
        tasks.append(task_name)

    print(f"Today's Tasks is \n {tasks}")
    
    while True:
        option = int(input("Select the option you want to do:\n1.Add\n2.Update\n3.Delete\n4.View\n5.exit/stop\n"))
        if option == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Your {add} task is added to your tasks list..!")
            
        elif option == 2:
            up = input("Enter the task name you want to update: ")
            if up in tasks:
                updated_task = input("Enter new task: ")
                idx = tasks.index(up)
                tasks[idx] = updated_task
                print(f"Your {up} task is updated successfully...!")
            else:
                print("Please enter valid name...!") 
        
        elif option == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                idx = tasks.index(del_val)
                del tasks[idx]
                print(f"Your {del_val} task is deleted successfully..!")    
            else:
                print("Please enter valid task name!")
        
        elif option == 4:
            print(f"Your total-tasks are: {tasks}")
            
        elif option == 5:
            print("Thank you, for using our Task-Management Program..!")
            break
        
        else:
            print("Please Enter valid option..!")       
                  
task()       
        