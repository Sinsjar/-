from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/akmand/datasets/master/iris.csv")

print(df)

scaler = MinMaxScaler()
df[['sepal_length_cm']] = scaler.fit_transform(df[['sepal_length_cm']])
scaler = StandardScaler()
df[['sepal_width_cm']] = scaler.fit_transform(df[['sepal_width_cm']])
print(df)
