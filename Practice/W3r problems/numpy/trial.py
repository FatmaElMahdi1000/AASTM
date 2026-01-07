import pandas as pd
import matplotlib.pyplot as pt
import numpy as np

df_original = pd.read_csv("employee_data (1).csv")
df = df_original.copy()
#STEP#1 Understand the data
# print(df.info())
# np.mean(df['Salary'])
# print(np.mean(df['Salary']))
# print(df.describe()) #stat of only the numerical data
# print(df.isna().sum()) #number of empty cells
# df.dropna()
# print(df.dropna()) #inplace=true
# print(df)

#STEP#2 Fix column names:
# convert columnNames to str, strip any extra spaces, make it lower
#Replace for(employee salary) to be (employee_salary)
df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))

#STEP#3 Handling missing/incorrect values:
#detect NaN (how many?) then decide: 1.drop 1.fill in with sth else
# print(df.isna().sum())
#salary cols are all nums expect 1 str cell. :) convert all to numeric valus and that 1 str to NaN
df['salary'] = pd.to_numeric(df['salary'], errors='coerce') #ABC became NaN
#let's fill NaN with the Median Salary(Not average/mean) as it's better be Median with skewed data مشوه
salary_median = df['salary'].median()
df['salary'] = df['salary'].fillna(salary_median)
#salary has a negative value_to fix: use upper limit/lower limit
df['salary'] = df['salary'].clip(25000, 50000).astype(int) #astype make sure the values are integers
#with CLIP function we're giving lower and upper limit,it will check values,
# if values less that 25000 it will set it as 25000
#if values more than 50000 it will make it 50000

#column date has a missing date, use "mode": most rep. date and fill in this cell with it
Rep_date = df['join_date'].mode()[0]
df['join_date'] = df['join_date'].fillna(Rep_date)
#Age col. has NaN, let's fill it with Median Age
Median_age = df['age'].median()
df['age'] = df['age'].fillna(Median_age).astype(int)
#Name col. has NaN Name, let's make it unknown
df['name'] = df['name'].fillna('unknown')
print(df)

#check duplicates and let's remove
print(df.duplicated()) #2 rows are duplicated
df.drop_duplicates(inplace=True)

df.to_csv('employee_data_cleaned.csv', index=False)



