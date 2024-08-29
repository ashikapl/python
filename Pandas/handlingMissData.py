# Handling Missing data in csv file using pandas functions in python
import pandas as pd

var = pd.read_csv("F:\\github\\python\\MissData.csv")
print(var.to_string())

print(var.dropna())