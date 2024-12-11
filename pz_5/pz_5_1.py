#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


def subtract_digit_sum(number):
    return number - sum_of_digits(number)


def count_steps_to_zero(number):
    steps = 0

    while number != 0:
        try:
            number = subtract_digit_sum(number)
            steps += 1
        except Exception as e:
            print(f"Произошла ошибка: {e}. Прекращаем выполнение.")
            return steps

    return steps


def validate_input():
    while True:
        try:
            n = int(input("Введите положительное число: "))
            if n < 0:
                print("Число должно быть положительным. Попробуйте еще раз.")
                continue
            return n
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    n = validate_input()
    result = count_steps_to_zero(n)
    print(f"Через {result} шагов получится ноль.")

