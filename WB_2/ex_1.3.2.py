"""Создать 5x5 матрицу со значениями в строках от 0 до 4. Для создания
необходимо использовать функцию arrange."""
import numpy as np

array = np.zeros((5, 5))
array += np.arange(5)
print(array)
