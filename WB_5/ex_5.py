"""Постройте модель множественной линейной регрессии для произвольных
данных из нескольких столбцов.Найдите коэффициенты
множественной регрессии. Постройте прогноз."""

import pandas as pd
from sklearn import metrics
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

url = 'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'

dataframe = pd.read_csv(url)
print(dataframe)

x = dataframe.iloc[:, :-1].values
y = dataframe.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = DecisionTreeRegressor()
regressor.fit(x_train, y_train)
tree.plot_tree(regressor)
y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

