import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = [random.randint(-10, 10) for _ in range(cols)]
    matrix.append(row)

print("\nСгенерированная матрица:")
for row in matrix:
    print(row)

modified = [row[:-1] + [-1] for row in matrix]

print("Матрица после замены:")
for row in modified:
    print(row)
