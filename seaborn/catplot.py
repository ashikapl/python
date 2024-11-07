# catplot --> which is a new version of factorplot with the help of which we can create 
# different types of plot --> box, strip, violin, swarm, count, bar, point, boxen etc use of (kind) function

import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips").head(100)
# print(data)

# hue parameter is used to differentiate the data
# height parameter is change the height of graph according to the given parameter
sns.catplot(x="day",y="size",data=data,hue="sex",palette="tab10",height=6,kind="point")
# Kind --> this parameter can plot strip, swarm, point, box, violin, boxen, count,
            # bar etc types of plots according to the given data
plt.show() 