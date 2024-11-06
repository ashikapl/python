# (PairPlot) :--> Subplot grid for more flexible plotting of pairwise relationships.
import seaborn as sns
from matplotlib import pyplot as plt

data = sns.load_dataset("tips").head(100)
print(data)

# sns.pairplot(data)

sns.pairplot(data, hue="sex",vars=["total_bill","tip"],palette="Paired",hue_order=["Female","Male"],markers=["*","^"])

# sns.pairplot(data, hue="sex",vars=["total_bill","tip"],palette="Paired",hue_order=["Female","Male"],kind="kde",diag_kind="hist")
# kde -> is lining on hist graphs

# sns.pairplot(data, hue="sex",x_vars=["total_bill","tip"])

# sns.pairplot(data, hue="sex",y_vars=["total_bill","tip"])
plt.show()