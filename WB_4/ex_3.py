"""Постройте модель линейной регрессии для произвольных данных из двух
столбцов. Найдите коэффициенты линии регрессии. Постройте прогноз"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = 'https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv'

dataframe = pd.read_csv(url)

x = dataframe.iloc[:, :-1].values
y = dataframe.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

plt.scatter(x_test, y_test, color='green')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.show()
