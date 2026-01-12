import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("dataset/sales_data.csv")

#print(data_frame)

# #list the columns in the dataset
# print(data_frame.columns)

# #Get top5 rows in the dataset
# print(data_frame.head(5))

##Get buttom 5 rows in the dataset
# print(data_frame.tail(5))

#Get only the productname, stock and price
#print(dataframe[["product_name", "price","stock"]])

# #Get info of that dataset
# print(data_frame.info())

#Dataset Discription
# print(data_frame.describe())

product_stocks = data_frame[["product_name", "stock"]]
product_stocks.plot()
plt.show()