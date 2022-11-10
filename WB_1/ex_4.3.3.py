"""Дана функция
Построить график на интервале (0,10)
с шагом 1 с заливкой площади и найти эту площадь
под ним. Для вычисления площади воспользуйте функции trapz(),
вычисляющей интеграл по правилу трапеции.
Для ее корректной работы необходимо подключить следующие
библиотеки:
from scipy.integrate import simps
from numpy import trapz"""
import numpy
from scipy.integrate import simps
from numpy import trapz
import matplotlib.pyplot as plt

x = numpy.arange(0, 11, 1)
y = numpy.abs(numpy.cos(x * numpy.exp(numpy.cos(x) + numpy.log1p(x))))

plt.plot(x, y)
plt.fill_between(x, y)
plt.show()

area = trapz(y)
print(area)
