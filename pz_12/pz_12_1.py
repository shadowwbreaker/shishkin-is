import random


def main():
    print("Обработка числовой последовательности")

    while True:
        try:
            n = int(input("Введите количество элементов: "))
            if n > 0:
                break
            print("Число должно быть больше 0!")
        except ValueError:
            print("Нужно ввести целое число!")

    sequence = [random.randint(-100, 100) for _ in range(n)]
    print(f"Исходная последовательность: {sequence}")

    positive_even = [x for x in sequence if x > 0 and x % 2 == 0]
    print(f"Положительные четные элементы: {positive_even}")

    if positive_even:
        sum_even = sum(positive_even)
        average = sum_even / len(positive_even)
        print(f"Сумма элементов: {sum_even}")
        print(f"Среднее арифметическое: {average:.2f}")
    else:
        print("Нет положительных четных элементов.")


if __name__ == "__main__":
    main()