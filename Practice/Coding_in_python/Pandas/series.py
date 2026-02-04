import pandas as pd
data = pd.read_csv("employee_data.csv")
data.to_csv("employee_data_backup.csv", index=False) #creating copy of the current xlsx before working on it
two_rows = data.head(2)
# print(data.drop_duplicates()) #removing duplicates
# print(data.describe()) #– Summarizes numeric columns with count, mean, std, min, max.
# print(data.info()) #Shows column names, types, and non-null counts.
# print(data.shape) #returns number of rows. columns
# print(data.columns) #print columns names
# print(data.index) #print index
new_info = {"Name": ["Fatma"], "Age": [29], "Salary" : [60000], "Gender": ["F"], "Join_Date" : ["12/2/2025"]}
#convering new_info to data frame first thing then concatenate it
new = pd.DataFrame(new_info)
data = pd.concat([data, new], ignore_index="True") #adding, ignore index, so the numbering be correct, even if we concatenated two dataframes
data.index = data.index + 1
#adding new info with loc (different way), len(data) to add at the end
data.loc[len(data)] = ["Mohamed", 32, 70000, "M", "15/10/2026"]
# print(data.isnull().sum()) #count missing data in each column
# salaries = data[['Salary']]
# print(salaries)
# print(data[data.duplicated()]) #show us the duplicates
data = data.drop_duplicates()
data = data.dropna()
# print(data[data.isna().any(axis=1)]) #print the data with Nan or N/A in it

data.to_csv("employee_data.csv", index=False)
print(data)