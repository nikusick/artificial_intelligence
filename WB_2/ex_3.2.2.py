"""Необходимо выполнить нормализацию первого числового признака
(sepal_length_cm) с использованием минимаксного преобразования, а
второго (sepal_width_cm) с задействованием z-масштабирования."""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

url = 'https://raw.githubusercontent.com/akmand/datasets/master/iris.csv'
dataframe = pd.read_csv(url)
print(dataframe)

scaler = MinMaxScaler()
dataframe[['sepal_length_cm']] = scaler.fit_transform(dataframe[['sepal_length_cm']])
print(dataframe)

dataframe['sepal_width_cm'] = (dataframe['sepal_width_cm'] - dataframe['sepal_width_cm'].mean()) \
                              / dataframe['sepal_width_cm'].std()


print(dataframe)
