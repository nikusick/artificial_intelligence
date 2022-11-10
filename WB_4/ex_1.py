"""Представьте собственные данные и постройте эктраполяцию полиномами
первой, второй и третьей степени."""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([4.5, 0.85, 4, 6])

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Исходные данные', markersize=10)
plt.plot(x, m * x + c, 'r')
plt.legend()
plt.show()

m = np.vstack((x ** 2, x, np.ones(len(x)))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_prec = np.linspace(0, 3, 101)
plt.plot(x, y, 'D')
plt.plot(x_prec, s[0] * x_prec ** 2 + s[1] * x_prec + s[2], '-', lw=2)
plt.grid()
plt.show()


m = np.vstack((x ** 3, x ** 2, x, np.ones(len(x)))).T
s = np.linalg.lstsq(m, y, rcond=None)[0]
x_prec = np.linspace(0, 3, 101)
plt.plot(x, y, 'D')
plt.plot(x_prec, s[0] * x_prec ** 3 + s[1] * x_prec ** 2 + s[2] * x_prec + s[3], '-', lw=3)
plt.grid()
plt.show()
