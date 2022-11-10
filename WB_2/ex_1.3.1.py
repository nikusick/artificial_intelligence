"""Создать 8x8 матрицу и заполнить её в шахматном порядке нулями и
единицами."""
import numpy as np

array = np.zeros((8, 8), dtype=int)
array[1::2, ::2] = 1
array[::2, 1::2] = 1
print(array)
