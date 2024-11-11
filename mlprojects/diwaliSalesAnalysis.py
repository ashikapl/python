# Diwali Sales --> Data Analysis Projext using Numpy, Pandas, Matplotlib and Seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# var = pd.read_csv("DiwaliSalesData.csv", header=None)
df = pd.read_csv("DiwaliSalesData.csv", encoding="ISO-8859-1") #df -> DataFrame(DataSet)
# to avoid encoding error for conversion to binary into human readable language
# print(df)

# DATA CLEANING 

# 1 --> check the shape of the dataset
print("Shape:->", df.shape)
print()

# info function is giving the informantion about the dataset -> dtype, isnull or notnull
print(df.info())

# drop function is remove the specific columns you are given with the (axis)
print(df.drop(["Status","unnamed1"], axis=1, inplace=True)) 
# Here we use (inplace) function to change in original array
print()

# print(df.info())
print("Shape:->",df.shape)
print()

# isnull -> check the null row or col it will give as True or False in output
print(pd.isnull(df))
print()

# it give the sum of all the null value according to the each row
print(pd.isnull(df).sum())

# drop null values
print(df.dropna(inplace=True))
print(pd.isnull(df).sum())
print()

# we can change dtype also of any row or col
print("DataType of Amount col before changing:-> ",df.dtypes["Amount"])
df["Amount"] = df["Amount"].astype(int)
print("DataType of Amount col after changing:-> ",df.dtypes["Amount"])
# print(df)

# Get column name
print(df.columns)

# rename specific col name
df.rename(columns={"Amount":"Money"}) # (inplace=True) is used for changing the original dataset 
print()
# print(df)

# describe ->> it give as count, mean, min, max, std, 25%, 75%, 50% of all the numeric values
print(df.describe())

# we can get describe function for specific columns
print(df[["Amount","Age","Orders"]].describe())

# EXPLORITORY DATA ANALYSIS --> Using Data visualization by making plot

# GENDER WISE ANALYSIS--

# Count the no of buyers (Female and Male) 
count_gen = sns.countplot(x="Gender", data=df, color="red",saturation=0.4)

for i in count_gen.containers:
    count_gen.bar_label(i)

plt.title("Count_Gen")
plt.show()

# Here we sum the amount value for male and female to analyis that who purchase more items
sales_gender = df.groupby(["Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
print()
print(sales_gender)
print()
sns.barplot(x="Gender",y="Amount",data=sales_gender,color="red",saturation=0.4)
plt.title("Sales_Gender")
plt.show()

print("ACCORDING TO GENDER GRAPHS")
print("Note:-> From the above graph we can see that most of the buyers are Female and the purchasing power of Female is greater than Male.")
print()

# AGE-GROUP WISE ANALYSIS--
# count the no. of buyers by age-group wise
# print(df.columns)
count_age = sns.countplot(x="Age Group",data=df,color="blue",saturation=0.2)

for i in count_age.containers:
    count_age.bar_label(i)
    
plt.title("Count_Age")
plt.show()

sales_age = df.groupby(["Age Group","Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sales_age = sns.barplot(x="Age Group", y="Amount",data=sales_age,hue="Gender",palette="dark:blue",saturation=0.2)

plt.title("Sales_Age")
plt.show()

print("ACCORDING TO AGE-GROUP GRAPH")
print("Note:-> From the above graph we can see that most of the buyers are females in age-group between 26-35.")
print()

# MARITAL STATUS WISE ANALYSIS--
count_Marital_status = sns.countplot(x="Marital_Status",data=df,color="pink")

for i in count_Marital_status.containers:
    count_Marital_status.bar_label(i)

plt.title("Count_Marital-Status")
plt.show()

sales_Marital_status = df.groupby(["Marital_Status","Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sales_Marital_status = sns.barplot(x="Marital_Status",y="Amount",data=sales_Marital_status,hue="Gender",palette="dark:pink")

plt.title("Sales_Material-Status")
plt.show()

print("ACCORDING TO MARITAL-STATUS GRAPH")
print("Note:-> From the above graph we can see that most of the buyers are married females.")
print()

# print(df.columns)

# STATE WISE ANALYSIS--
orders_state = df.groupby(["State"], as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(7)

sns.set(rc={"figure.figsize":(11,4)})
sns.barplot(x="State",y="Orders",data=orders_state,color="yellow",saturation=0.6)

plt.title("Sales_State")
plt.show()


sales_state = df.groupby(["State"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False).head(7)

sns.set(rc={"figure.figsize":(11,4)})
sns.barplot(x="State",y="Amount",data=sales_state,color="yellow",saturation=0.6)

plt.title("Sales_State")
plt.show()

print("ACCORDING TO STATE GPRAH")
print("Note:-> From the above graph we can see that the most of the orders and high purchasing power from Uttar-Pradesh, Maharashtra and Karnataka.")
print()

# print(df.columns)
# OCCUPATION WISE ANALYSIS
sns.set(rc={"figure.figsize":(11,4)})
count_occup = sns.countplot(x="Occupation",data=df,color="violet")

for i in count_occup.containers:
    count_occup.bar_label(i)

plt.xticks(fontsize=6.10)
plt.title("Count-Occupation")
plt.show()

sales_occup = df.groupby(["Occupation"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sns.barplot(x="Occupation",y="Amount",data=sales_occup,color="violet")

plt.xticks(fontsize=6.10)
plt.title("Sales-Occupation")
plt.show()

print("ACCORDING TO OCCUPATION GRAPH")
print("Note:-> From the above graph we can see that most of the buyers in IT-Sector, Aviation and Health-Care.")
print()

# print(df.columns)
# PRODUCT-CATEGORY WISE ANALYSIS
sns.set(rc={"figure.figsize":(13,5)})
count_prod = sns.countplot(x="Product_Category",data=df)

for i in count_prod.containers:
    count_prod.bar_label(i)
    
plt.xticks(fontsize=5)
plt.title("Count-Product-Category")
plt.show()

sales_prod = df.groupby(["Product_Category"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sns.barplot(x="Product_Category", y="Amount", data=sales_prod)

plt.xticks(fontsize=5)
plt.title("Sales-Product-Category")
plt.show()

print("ACCORDING TO PRODUCT-CATEGORY GRAPH")
print("Note:-> From the above graph we can see that most of the buyers in Clothing-Apparel, Food and electronics-gadgets.")
print()

# print(df.columns)
# PRODUCT_ID WISE ANANLYSIS
sns.set(rc={"figure.figsize":(10,4)})
sales_pro_id = df.groupby(["Product_ID"], as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False).head(10)

sns.barplot(x="Product_ID", y="Orders",data=sales_pro_id,color="Purple")

plt.xticks(fontsize=6)
plt.title("Sales-Product-Id")
plt.show()

print("ACCORDING TO PRODICT_ID GRAPH")
print("Note:-> From the above graph we can see that most of the buyers in P00265242.")
print()
print()

print("""CONCLUSION::- Married womens age group between 26-35 years from UP, Maharashtra and Karnataka working in 
              IT-Sector, Health-Care and Aviation are more likely in buying clothes, food and electronics category!""")