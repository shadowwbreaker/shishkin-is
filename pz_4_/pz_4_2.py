# Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
# увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
# <25). По данному P определить, через сколько месяцев размер вклада превысит 1100
# руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
# вклада S (вещественное число).

def calculate_months_and_amount(P):
    initial_deposit = 1000
    target_deposit = 1100

    months = 0
    current_deposit = initial_deposit

    while current_deposit < target_deposit:
        current_deposit *= (1 + P / 100)
        months += 1

    return months, round(current_deposit, 2)


while True:
    try:
        P = float(input("Введите процент увеличения вклада (от 0 до 25): "))
        if not (0 <= P <= 25):
            raise ValueError("Процент должен быть между 0 и 25")

        months, final_amount = calculate_months_and_amount(P)
        print(f"Через {months} месяцев размер вклада составит {final_amount} рублей.")
        break

    except ValueError as e:
        print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")

