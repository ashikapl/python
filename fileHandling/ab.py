# write in the file if not exists then create the file and in write command it will remove the pehle wala data
# f = open("demofile2.txt", "w")
# f.write("I am good.")
# f.close()

# read in file
# f = open("demofile2.txt", "r")
# print(f.read())

# chech and remove the file
# import os
# if os.path.exists("demofile.text"):
#     os.remove("demofile.text")
# else:
#     print("the file is not exists")

# delete empty folder
# import os
# os.rmdir("myfolder")

# append in file  if file not exists then it create automatically and it will add the data in that file
# if file is already exists
a = open("example.txt", 'a')
a.write("good luck!")
a.close()

a = open("example.txt", 'r')
print(a.read())
a.close()