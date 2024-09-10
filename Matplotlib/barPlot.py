import matplotlib.pyplot as plt

a = ['Python','C++','Java','Js']
b = [60,50,45,42]


l1 = plt.xlabel('Language',fontsize=20)
l2 = plt.ylabel('No.',fontsize=20)
t = plt.title('Ranks',fontsize=20)
x = plt.bar(a,b,width=0.5)
plt.show()