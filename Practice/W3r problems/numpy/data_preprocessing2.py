import pandas as pd
#data integration #integrate more that one csv in the same dataframe

jan = pd.read_csv("sales_jan.csv")
Feb = pd.read_csv("sales_feb.csv")

# merged=pd.concat([jan, Feb], ignore_index=True).drop_duplicates() #ignore index to avoid, keeping the same indcies of the old dataframes
#
# print(merged)
