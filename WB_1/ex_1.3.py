"""Выведите на печать и определите тип переменной."""

from tabulate import tabulate

x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34, 'ж'
z = 'type'
D = [1, 'title', 2, 'content']

print(
    tabulate(
        [[x, type(x)], [A, type(A)],
         [B, type(B)], [C, type(C)],
         [df, type(df)], [z, type(z)], [D, type(D)]],
        headers=['Value', 'Type'], tablefmt='orgtbl'
    )
)
