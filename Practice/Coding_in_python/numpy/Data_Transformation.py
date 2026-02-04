import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
#Data transformation is converting raw data into a format machines can work with.
#label Encoding (label encoder function) ; Raw data is messy. Models don’t “understand” text, categories, dates, or missing values.
#They understand numbers arranged in a strict structure.
order = pd.read_csv("orders.csv")
cust = pd.read_csv("customers.csv")
merged = pd.merge(cust, order, on="CustomerID", how="inner")
le= LabelEncoder()
merged['City'] = le.fit_transform(merged['City'])
print(merged)

