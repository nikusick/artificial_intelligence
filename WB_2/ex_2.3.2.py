"""Найдите в Интернете ссылку на любой csv файл и сформируйте из него
фрейм данных"""

import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/diamonds.csv'
dataframe = pd.read_csv(url)
print(dataframe)
