import matplotlib.pyplot as plt
import numpy as np

a = ['Python','C++','Java','Js']
b = [87,70,60,82]
# c = [20,30,40,50]


l1 = plt.xlabel('Language',fontsize=15)
l2 = plt.ylabel('No.',fontsize=15)
t = plt.title('Ranks',fontsize=15)
c = ['b','g','r','y']
# x = plt.bar(a,b,width=0.5, color=c, align='edge', edgecolor='black', linewidth=2, linestyle=':',alpha=0.9)
# alpha value is use btwn 0 to 1 for brightness
# linewidth is for boundary line of graph plots and
# linestyle is for dotted or simple line around the plots
# we can use center also in align parameter to keep the (a) list point at center
width=0.5
x = plt.bar(a,b,width, color='brown', edgecolor = 'black', label="Popularity")
# x = plt.bar(a,c,width, color='b', edgecolor = 'green', label="Popularity1")
plt.legend()
plt.show()

x = ['A','B','C','D','E']
y = [22,23,43,34,25]
z = [12,13,24,18,22]

ypos = np.arange(len(x))
# here by sub and add 0.2  with ypos to separate them
plt.barh(ypos-0.2,y,height=0.4, label='Revenue') # btwn (0-1)
plt.barh(ypos+0.2,z,height=0.4, label='Profit')
plt.legend() # here legend is used for label showing 
plt.show()