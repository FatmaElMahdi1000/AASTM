#machines/ machines algorithms are not reading any strings, it needs numerics only
#so we convert the data to something the machines understanding
#solution: label transform, label encoding, transforming every string to a number
import pandas as pd
from sklearn.preprocessing import LabelEncoder


customer = pd.read_csv("customers.csv")
order = pd.read_csv("orders.csv")
df = pd.merge(customer, order, on="CustomerID", how="inner") #merge with any key, column (on=customerID)
df.columns = df.columns.str.strip() #to remove extra spaces in the string names
le = LabelEncoder()
df["City"]=le.fit_transform(df["City"])
print(df)


