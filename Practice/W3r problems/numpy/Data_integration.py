#Combine data from multiple sources
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

# jan = pd.read_csv("sales_jan.csv")
# feb = pd.read_csv("sales_feb.csv")
# merged = pd.concat([jan, feb], ignore_index=True).drop_duplicates() #if added inplace=True, it will return none, better to remove
# print(merged)

#combining 2 data frames using primarykey/forign key, if the 2 DF are with different no. of columns
order = pd.read_csv("orders.csv")
cust = pd.read_csv("customers.csv")
#linking 2 Data Frames with relations: we'll use merge func in that case not concat, as we're linking with pk
#relation on what ??? on=cust_id CustomerID must be a column name that exists in BOTH DataFrames.
#inner will ignore the missing data,will only display the order IDs and Customer IDs with relations and
#ignore any others with no relations like: Cust_ID 106
# merged = pd.merge(cust, order, on="CustomerID", how="inner")
# print(merged)
#how="outer" Keeps everything from both tables even if no relation
#how="left" keeps all customers (our customer ID)
#how="right" keeps all orders
merged = pd.merge(cust, order, on="CustomerID", how="outer")
# merged = pd.merge(cust, order, on="CustomerID", how="left") #left here (cust (left data Frame), order(right df))
# merged = pd.merge(cust, order, on="CustomerID", how="right")#Right here; right data frames (cust (left data Frame), order(right df))
#
