"""Создайте массив и отсортируйте его по убыванию."""

import numpy as np

array = np.random.randint(1, 10, 5)
array = sorted(array, reverse=True)
print(array)
