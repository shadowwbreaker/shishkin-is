import datetime


class Calendar:
    def __init__(self, year, month, day):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год должен быть положительным целым числом.")
        if not isinstance(month, int) or month < 1 or month > 12:
            raise ValueError("Месяц должен быть целым числом от 1 до 12.")
        if not isinstance(day, int) or day < 1 or day > 31:
            raise ValueError("День должен быть целым числом от 1 до 31.")

        try:
            datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Некорректная дата: {e}")

        self.year = year
        self.month = month
        self.day = day

    def get_weekday(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        weekday = datetime.date(self.year, self.month, self.day).weekday()
        return days[weekday]

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def days_in_month(self):
        if self.month == 2:
            return 29 if self.is_leap_year() else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


if __name__ == "__main__":
    test_dates = [
        (2023, 10, 15),
        (2024, 2, 29),
        (2021, 4, 30),
        (2000, 1, 1),
        (1900, 2, 28),
    ]

    for year, month, day in test_dates:
        try:
            print(f"\nДата: {day:02d}.{month:02d}.{year}")
            cal = Calendar(year, month, day)
            print(f"День недели: {cal.get_weekday()}")
            print(f"Високосный год: {'Да' if cal.is_leap_year() else 'Нет'}")
            print(f"Дней в месяце: {cal.days_in_month()}")
        except ValueError as e:
            print(f"Ошибка: {e}")