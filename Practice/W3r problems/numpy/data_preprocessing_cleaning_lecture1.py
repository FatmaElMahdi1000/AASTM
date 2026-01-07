import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder


#from CSV to dataframe
df = pd.read_csv("employee_data (1).csv")
# print(df.shape) #no.of rows and columns
# df.info() #general info on dataframe
# print(df.dtypes)
# print(df.describe()) #statistical info on the numerical cols only
# print(df.isna().sum()) #cells that are NaN (empty cells)
# df.dropna(inplace=True) #to drop

#convert strings in salaries to numerical values, and it will convert any strings to Nan values

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
mean_salary = df['Salary'].mean()
#salary average
median_value_age = df["Age"].median() #specify the column of the mean, median value to avoid the decimal of the mean
mode_value_date = df["Join_Date"].mode()[0] #save value in idx 0 #the most repetitive date to fill the nan values in the date column
df["Name"]=df["Name"].fillna("Unknown")
df["Salary"]=df["Salary"].fillna(value=mean_salary)
df["Age"]=df["Age"].fillna(value=median_value_age)
df["Join_Date"] = df["Join_Date"].fillna(value=mode_value_date)
#giviing the salary lower limit and upper limit to avoid present -ve values
df["Salary"]=df["Salary"].clip(25000,80000)
#to know if there's a duplicate
# print(df.duplicated())
# updated_df = df.drop_duplicates() #instead of updating the present df, it creates a copy with the new output
# print(updated_df)

#data scaling: It rescales numeric data so models don’t get biased by large values.
le=LabelEncoder()
df["Salary"]=le.fit_transform(df[["Salary"]])
scaler = MinMaxScaler()
df["Salary"] = scaler.fit_transform(df[['Salary']])
