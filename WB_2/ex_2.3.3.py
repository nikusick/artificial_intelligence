"""Проделайте с получившемся из предыдущего задания фреймом данных
те же действия, что и в примерах 2.2.5-2.2.7."""

import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/diamonds.csv'
dataframe = pd.read_csv(url)
print('Head:\n', dataframe.head(2))
print('Tail:\n', dataframe.tail(3))
print('Shape:\n', dataframe.shape)
print('Describe:\n', dataframe.describe())

print('Iloc:\n', dataframe.iloc[1:4])
print('Diamonds with color "E"\n', dataframe[dataframe['color'] == 'E'])
