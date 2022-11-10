"""Создайте матрицу, выведите ее форму, размер и размерность."""

import numpy as np

array = np.arange(9).reshape(3, 3)
print(array)
print('Форма:', array.shape)
print('Размерность:', array.itemsize * array.size)
print('Размер:', array.shape)
