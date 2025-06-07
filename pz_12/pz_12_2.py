def lowercase_generator(input_string):
    for char in input_string:
        yield char.lower()


def main():
    print("Преобразование строки в нижний регистр")
    input_string = input("Введите строку: ")

    generator = lowercase_generator(input_string)
    result = ''.join([char for char in generator])

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()