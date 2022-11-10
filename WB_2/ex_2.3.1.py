"""Найдитн евклидово расстояние между двумя Series (точками) a и b, не
используя встроенную формулу."""

import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([5, 4, 3, 2, 1])
distance = np.sqrt(sum(pow(a-b, 2) for a, b in zip(s1, s2)))
print(distance)
