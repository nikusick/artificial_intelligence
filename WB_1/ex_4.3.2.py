"""Дана функция
Создать массив из 10 значений
функции (𝑥, например, изменяется от 1 до 10). Выделить срез первой
половины массива и построить графики для основного массива –
линейный и для среза – точечный"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11, 1)
y = np.sqrt(1 + np.e ** np.sqrt(x) + np.cos(x ** 2)) \
    / (np.abs(1 - np.sin(x) ** 3)) \
    + np.log(np.abs(2 * x))

fig = plt.figure(figsize=(10, 7))
plt.plot(x, y)
plt.show()
plt.scatter(x[0:6], y[0:6])
plt.show()
