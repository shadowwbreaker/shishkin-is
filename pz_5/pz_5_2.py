#Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
#числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
#1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
#С помощью этой функции последовательно добавить к данному числу K слева
#данные цифры D1 и D2, выводя результат каждого добавления.

def AddLeftDigit(D, K):
    """
    Добавляет к числу K слева цифру D.

    :param D: Цифра для добавления (целое число от 1 до 9)
    :param K: Исходное число (целое число)
    :return: Новое число с добавленной слева цифрой D
    """
    if not isinstance(D, int) or not 1 <= D <= 9:
        raise ValueError("Параметр D должен быть целым числом в диапазоне от 1 до 9")
    if not isinstance(K, int):
        raise ValueError("Параметр K должен быть целым числом")

    return D * 10 + K

def get_valid_int(prompt, min_value=None, max_value=None):
    """
    Запрашивает у пользователя целое число и проверяет его на соответствие указанным ограничениям.

    :param prompt: Сообщение для вывода пользователю
    :param min_value: Минимальное допустимое значение (необязательно)
    :param max_value: Максимальное допустимое значение (необязательно)
    :return: Корректное целое число
    """
    while True:
        try:
            value = int(input(prompt))
            if ((min_value is None or value >= min_value) and
                    (max_value is None or value <= max_value)):
                return value
            else:
                print(f"Введено неправильное значение. Оно должно быть в диапазоне от {min_value} до {max_value}.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")

def main():
    try:
        K = get_valid_int("Введите исходное число K: ")
        D1 = get_valid_int("Введите первую цифру D1 для добавления: ", 1, 9)
        D2 = get_valid_int("Введите вторую цифру D2 для добавления: ", 1, 9)

        new_K = AddLeftDigit(D1, K)
        print(f"После добавления цифры {D1}: {new_K}")

        final_result = AddLeftDigit(D2, new_K)
        print(f"После добавления цифры {D2}: {final_result}")
    except ValueError as e:
        print(f"Произошла ошибка: {e}. Пожалуйста, проверьте введенные значения.")

if __name__ == "__main__":
    main()

