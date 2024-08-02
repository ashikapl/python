import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"Filename {filename}: created successfully!")
    except FileExistsError:
        print(f"{filename}: is already exists!")   
    except Exception as E:
        print("An error occurred!")

def view_all_file():
    files = os.listdir()
    
    if not files:
        print("No file found!")
    else:
        print("Files in Directory")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename}: is deleted successfully!")
    except FileNotFoundError:
        print(f"This {filename}: File not exists!")
    except Exception as e:
        print("An error occurred!")
        
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' : \n {content}")
    except FileNotFoundError:
        print(f"This {filename}: File not exists!")
    except Exception as e:
        print("An error occurred!")
            
def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter to add data = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully!")
    except FileNotFoundError:
        print(f"This {filename}: File not exists!")
    except Exception as e:
        print("An error occurred!") 
        
def main():
    while True:
        print("...File Management App...")  
        print("1. Create a file")
        print("2. View all files")
        print("3. Delete the file")
        print("4. Read the file")
        print("5. Edit the file")
        print("6. Exit")
        
        choice = input("Enter your choice(1-6):= ")
        
        if choice == '1':
            filename = input("Enter the file-name you want to create:= ")
            create_file(filename)
        elif choice == '2':
            view_all_file()
        elif choice == '3':
            filename = input("Enter the file-name you want to delete:= ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file-name you want to read:= ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file-name you want to edit:= ")
            edit_file(filename)
        elif choice == '6':
            print("Closing the App...!")
            break
        else:
            print("Invalid Choice..!")

if __name__  == "__main__":
    main()
    
    
    
        
    