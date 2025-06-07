import random


def replace_third_row():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    if rows >= 3:
        n = len(matrix[0])
        new_row = [random.randint(10, 20) for _ in range(n)]

        print(f"\nНовая строка: {new_row}")

        modified = [row if i != 2 else new_row for i, row in enumerate(matrix)]

        print("\nМатрица после замены третьей строки:")
        for row in modified:
            print(row)
    else:
        print("\nВ матрице меньше 3 строк, замена невозможна")


if __name__ == "__main__":
    replace_third_row()
