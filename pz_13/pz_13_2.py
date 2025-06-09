#В двумерном списке элементы третьей строки заменить элементами из одномерного
#динамического массива соответствующей размерности.
import random


def replace_third_row():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    n = len(matrix[0])
    new_row = [random.randint(10, 20) for _ in range(n)]

    print(f"Новая строка: {new_row}")

    modified = [row if i != 2 else new_row for i, row in enumerate(matrix)]

    print("Матрица после замены:")
    for row in modified:
        print(row)


if __name__ == "__main__":
    replace_third_row()