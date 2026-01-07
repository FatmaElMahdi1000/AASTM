#if adding 2 files that are not identical, different number of columns
import pandas as pd

customer = pd.read_csv("customers.csv")
order = pd.read_csv("orders.csv")
#connecting the 2 files using the customer ID, even if the files/dataframes will be not identical
merged = pd.merge(customer, order, on="CustomerID", how="inner") #merge with any key, column (on=customerID)
print(merged)