"""Подставьте собственные данные и поэкспериментируйте с представленными
функциями. Проанализируйте динамику изменения данных."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

beta = (1, 2)


def f1(x, b0, b1):
    return x ** 2 * b0 + b1


x_data = np.linspace(0, 5, 50)
y = f1(x_data, *beta)
y_data = y + 0.05 * np.random.randn(len(x_data))
beta_opt, beta_cov = curve_fit(f1, x_data, y_data)

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f1(x_data, *beta_opt), 'b', lw=2)
plt.show()

beta = (1, 2, 0.5)


def f2(x, b0, b1, b2):
    return x ** 3 * b0 + b1 * x ** 2 + b2


x_data = np.linspace(0, 5, 50)
y = f2(x_data, *beta)
y_data = y + 0.05 * np.random.randn(len(x_data))
beta_opt, beta_cov = curve_fit(f2, x_data, y_data)

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_data, y, 'r', lw=2)
ax.plot(x_data, f2(x_data, *beta_opt), 'b', lw=2)
plt.show()
