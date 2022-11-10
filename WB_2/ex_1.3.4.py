"""Создать матрицу с 0 внутри, и 1 на границах."""

import numpy as np

array = np.ones((5, 5))
array[1:-1, 1:-1] = 0
print(array)
