def replace_last_column():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    modified = [row[:-1] + [-1] for row in matrix]

    print("Матрица после замены:")
    for row in modified:
        print(row)


if __name__ == "__main__":
    replace_last_column()