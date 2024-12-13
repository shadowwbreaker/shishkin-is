#Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
#наименьший периметр треугольника, вершины которого принадлежат различным
#точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
#они перечислены при задании множества A).
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2.
#Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй — для хранения ординат.


import random
from itertools import combinations  #Импортируем функцию для создания комбинаций
from math import sqrt  #Импортируем функцию для вычисления квадратного корня


def generate_random_coordinates(n):

    points_x = [random.uniform(-100, 100) for _ in range(n)]  #Генерация списка случайных координат X
    points_y = [random.uniform(-100, 100) for _ in range(n)]  #Генерация списка случайных координат Y
    return points_x, points_y  #Возвращаем два списка координат


def distance(x1, y1, x2, y2):

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)  #Используем формулу Евклида для расчета расстояния


def perimeter(points_x, points_y, idx1, idx2, idx3):

    d1 = distance(points_x[idx1], points_y[idx1], points_x[idx2], points_y[idx2])  # Расчет длины стороны 1
    d2 = distance(points_x[idx2], points_y[idx2], points_x[idx3], points_y[idx3])  # Расчет длины стороны 2
    d3 = distance(points_x[idx3], points_y[idx3], points_x[idx1], points_y[idx1])  # Расчет длины стороны 3
    return d1 + d2 + d3  #Сумма длин сторон дает периметр треугольника


def smallest_perimeter_triangle(points_x, points_y):

    n = len(points_x)  #Определяем количество точек
    min_perim = float('inf')  #Устанавливаем начальное значение минимального периметра как бесконечность
    result_points = []  #Создаем пустой список для хранения координат вершин

    for comb in combinations(range(n), 3):  #Проходимся по всем возможным комбинациям троек индексов
        perim = perimeter(points_x, points_y, *comb)  #Рассчитываем периметр текущего треугольника
        if perim < min_perim:  #Если найден меньший периметр
            min_perim = perim  #Обновляем минимальное значение
            result_points = [(points_x[i], points_y[i]) for i in comb]  #Сохраняем координаты вершин

    return min_perim, result_points  #Возвращаем минимальный периметр и координаты вершин


def main():

    try:
        N = int(input("Введите количество точек N (N > 2): "))  #Запрашиваем у пользователя количество точек
        if N <= 2:  # Проверяем, что количество точек больше двух
            raise ValueError("Количество точек должно быть больше 2")  #Если условие нарушено, выбрасываем ошибку

        points_x, points_y = generate_random_coordinates(N)  #Генерируем случайные координаты точек

        min_perim, triangle_points = smallest_perimeter_triangle(points_x, points_y)  #Находим минимальный периметр

        print("\nКоординаты точек:")  #Выводим заголовок
        for i in range(N):  #Проходим по всем точкам
            print(f"{i+1}. ({points_x[i]:.2f}, {points_y[i]:.2f})")  #Выводим каждую точку с номером и координатами

        print(f"\nНаименьший периметр треугольника: {min_perim:.2f}")  #Выводим минимальный периметр
        for i, point in enumerate(triangle_points):  #Проходим по вершинам треугольника
            print(f"Вершина {i+1}: ({point[0]:.2f}, {point[1]:.2f})")  #Выводим координаты каждой вершины

    except ValueError as e:  #Обрабатываем возможные ошибки
        print(f"Произошла ошибка: {e}")  #Сообщение об ошибке


if __name__ == "__main__":
    main()  #Вызов основной функции при запуске скрипта
