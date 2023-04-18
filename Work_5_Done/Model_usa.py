import pandas as pd


url = 'https://raw.githubusercontent.com/likarajo/petrol_consumption/master/data/petrol_consumption.csv'

dataframe=pd.read_csv(url)

dataframe.head()

print(dataframe.shape)

print(dataframe.describe())

