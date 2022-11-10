"""Задайте массив случайных значений из интервала(0; 1).
Рассчитайте средние и медианные значения для массива, сравните
результаты, какие выводы можно сделать о значениях?
Постройте точечную диаграмму рассения полученного ряда"""
import statistics
import matplotlib.pyplot as plt
import numpy

massiv = numpy.random.random(5)
print('Массив:', massiv)
print('Среднее значение:', statistics.mean(massiv))
print('Медиана:', statistics.median(massiv))
plt.scatter([i for i in range(1, 6)], massiv)
plt.show()
