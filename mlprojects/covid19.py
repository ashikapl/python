# Covid-19 Data Analysis 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("F:/github/python/mlprojects/covid-19Data.csv")
# print(df)
# print()

# # DATA CLEANING -> PANDAS

# # Shape of dataSet
# print("Shape of df:-",df.shape)
# print()

# # info about all the columns with its datatype
# print(df.info())
# print()

# # Check the null value
# print(pd.isnull(df).sum())
# print()

# # Convert the dtype float into int
# print("Total Confirmed cases dtype before change:-",df.dtypes["Total Confirmed cases"])
# df["Total Confirmed cases"] = df["Total Confirmed cases"].astype(int)
# print("Total Confirmed cases dtype after change:-",df.dtypes["Total Confirmed cases"])
# print()
# # print(df.columns)

# # Convert the dtype float into int
# print("Cured/Discharged/Migrated dtype before change:-",df.dtypes["Cured/Discharged/Migrated"])
# df["Cured/Discharged/Migrated"] = df["Cured/Discharged/Migrated"].astype(int)
# print("Cured/Discharged/Migrated dtype after change:-",df.dtypes["Cured/Discharged/Migrated"])
# print()

# DATA VISUALIZATION -> MATPLOTLIB AND SEABORN 
# print(df.columns)

# State / UT(united State) wise analysis who has more test case
state_df = df.head(70)
sns.set(rc={"figure.figsize":(10,4)})
count_state = sns.countplot(x="Name of State / UT", data=state_df)

for i in count_state.containers:
    count_state.bar_label(i)
    
plt.xticks(fontsize=5)
plt.title("Count-State")
plt.show()

confirmedCases_df = df.groupby(["Name of State / UT"], as_index=False)["Total Confirmed cases"].sum().sort_values(by="Total Confirmed cases", ascending=False).head(10)
sns.barplot(x="Name of State / UT", y="Total Confirmed cases",data=confirmedCases_df)

plt.xticks(fontsize=5)
plt.title("State wise Confirmed-Cases")
plt.show()

print()
print("ACCORDING TO STATE WISE TEST-CASES")
print("Note:-> From the above graph we can see that most of the Confirmed Cases are from Kerala.")
print()

