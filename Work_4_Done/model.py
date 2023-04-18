import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"

df = pd.read_csv(url)


print(df)

print(df.shape)

print(df.describe())

plt.scatter(df['YearsExperience'],df["Salary"],color = 'r',label = "Salary data ")

plt.xlabel("YearsExperience")
plt.ylabel("Salary")

plt.show()

X =df.iloc[:,:-1].values
y = df.iloc[:,1].values

print(X)
print(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.2,random_state=0)

regressor = LinearRegression()
print(regressor)

regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

y_pred =regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test,"Predicted": y_pred})


df.plot(kind = 'bar')
plt.grid(which='major', linestyle = '-', linewidth ='0.5', color = 'green')
plt.grid(which='minor', linestyle = ':', linewidth ='0.5', color = 'black')
plt.show()

plt.scatter(X_test,y_test,color = 'gray')
plt.plot(X_test,y_pred,color = 'red', linewidth= 2)
plt.show()
