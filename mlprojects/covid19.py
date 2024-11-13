# Covid-19 Data Analysis 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("F:/github/python/mlprojects/covid-19Data.csv")
# print(df)
new_df = df.head(100)
# print()

# DATA CLEANING -> PANDAS

# Shape of dataSet
print("Shape of df:-",df.shape)
print()

# info about all the columns with its datatype
print(df.info())
print()

# Check the null value
print(pd.isnull(df).sum())
print()

# Convert the dtype float into int
print("Total Confirmed cases dtype before change:-",df.dtypes["Total Confirmed cases"])
df["Total Confirmed cases"] = df["Total Confirmed cases"].astype(int)
print("Total Confirmed cases dtype after change:-",df.dtypes["Total Confirmed cases"])
print()
# print(df.columns)

# Convert death column dtype float into int
# Print the dtype before conversion
print("Death dtype before change:", df.dtypes["Death"])

# Attempt to convert 'Death' to numeric, identifying problematic values
df["Death"] = pd.to_numeric(df["Death"], errors='coerce')

# Instead of using inplace=True, assign back to the 'Death' column
df["Death"] = df["Death"].fillna(0)

# Now safely convert the 'Death' column to integers
df["Death"] = df["Death"].astype(int)

# Print the dtype after conversion
print("Death dtype after change:", df.dtypes["Death"])
print()


# Convert the dtype float into int
print("Cured/Discharged/Migrated dtype before change:-",df.dtypes["Cured/Discharged/Migrated"])
df["Cured/Discharged/Migrated"] = df["Cured/Discharged/Migrated"].astype(int)
print("Cured/Discharged/Migrated dtype after change:-",df.dtypes["Cured/Discharged/Migrated"])
print()


# DATA VISUALIZATION -> MATPLOTLIB AND SEABORN 
# print(df.columns)

# new_df = df.head(100)

# State / UT(united State) wise analysis who has more test case
sns.set(rc={"figure.figsize":(10,4)})
count_state = sns.countplot(x="Name of State / UT", data=new_df, color="red",saturation=0.6)

for i in count_state.containers:
    count_state.bar_label(i)
    
plt.xticks(fontsize=5)
plt.title("Count-State")
plt.show()

print()
print("ACCORDING TO STATE WISE")
print("Note:-> From the above graph we can see that most of the patient are from Kerala.")
print()

# Confirmed-Cases according to state
confirmedCases_df = df.groupby(["Name of State / UT"], as_index=False)["Total Confirmed cases"].sum().sort_values(by="Total Confirmed cases", ascending=False).head(10)
sns.barplot(x="Name of State / UT", y="Total Confirmed cases",data=confirmedCases_df,color="purple",saturation=0.8)

plt.xticks(fontsize=5)
plt.title("State wise Confirmed-Cases")
plt.show()

print("ACCORDING TO STATE WISE TEST-CASES")
print("Note:-> From the above graph we can see that most of the confirmed cases are from Kerala.")
print()

# Deaths according to state
# After changing its dtype from float into int then the plot is create correctly
death_df = df.groupby(["Name of State / UT"], as_index=False)["Death"].sum().sort_values(by="Death", ascending=False).head(10)
# print(death_df)
sns.barplot(x="Name of State / UT", y="Death",data=death_df,color="blue",saturation=0.4)

plt.xticks(rotation=45, fontsize=8)  # Rotate x-axis labels by 45 degrees for better clarity
plt.title("State wise Deaths")
plt.show()

print()
print("ACCORDING TO STATE WISE DEATHS")
print("Note:-> From the above graph we can see that most of the deaths from Maharashtra.")
print()

# Cured/Discharged/Migrated according to state wise(CDM)
curedDM_df = df.groupby(["Name of State / UT"], as_index=False)["Cured/Discharged/Migrated"].sum().sort_values(by="Cured/Discharged/Migrated", ascending=False).head(10)
sns.barplot(x="Name of State / UT", y="Cured/Discharged/Migrated", data=curedDM_df, color="violet")

plt.xticks(rotation=45, fontsize=8)
plt.title("State wise Cured/Discharged/Migrated")
plt.show()

print("ACCORDING TO STATE WISE CDM(CURED/DISCHARGED/MIGRATED)")
print("Note:-> From the above graph we can see that most the CDM people from Maharashtra.")
print()

# print(new_df.columns)
# Now we have to compare old test cases and new cases trends
# sns.lineplot(x="Name of State / UT", y="Total confirmed cases",data=new_df)
# sns.lineplot(x="Name of State / UT", y="New cases", data=new_df)

# plt.title("Trends over old and new cases")
# plt.show()
# print(new_df.info())

# Trends btwn old and new deaths according to state wise
# plt.figure(figsize=(10, 6))
data = df.head(200)
sns.lineplot(x="Name of State / UT", y="Death", marker='o', data=data, label="Death")
sns.lineplot(x="Name of State / UT", y="New deaths", marker='o', data=data, label="New deaths")

plt.xticks(fontsize=8, rotation=45)
plt.title("Trend Comparison between Death and New Death")
plt.xlabel("State")
plt.ylabel("Count")
# plt.legend()
plt.show()

melted_df = df.melt(id_vars="Name of State / UT", value_vars=["Death","New deaths"], var_name="new", value_name="Count").head(200)
sns.barplot(x="Name of State / UT", y="Count", hue="new", data=melted_df)

plt.xticks(fontsize=8, rotation=45)
plt.title("Compare between Death and New Death")
plt.show()