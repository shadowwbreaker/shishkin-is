#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Количество элементов, общих для двух файлов:
#Количество четных элементов первого файла:
#Количество нечетных элементов второго файла:
def process_number_files():
    try:
        with open('file1.txt', 'w', encoding='utf-8') as f1:
            f1.write("12 -5 8 -3 17 0 -9 4 21")

        with open('file2.txt', 'w', encoding='utf-8') as f2:
            f2.write("-7 14 0 3 -2 8 19 -5 12 -1")

        def read_numbers(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return [int(num) for num in f.read().split()]

        nums1 = read_numbers('file1.txt')
        nums2 = read_numbers('file2.txt')

        avg1 = sum(nums1) / len(nums1) if nums1 else 0
        avg2 = sum(nums2) / len(nums2) if nums2 else 0

        odd_count1 = sum(1 for num in nums1 if num % 2 != 0)
        odd_count2 = sum(1 for num in nums2 if num % 2 != 0)

        common_elements = set(nums1) & set(nums2)
        common_count = len(common_elements)

        with open('result.txt', 'w', encoding='utf-8') as result_file:
            result_file.write("Элементы первого и второго файлов:\n")
            result_file.write(f"Первый файл: {', '.join(map(str, nums1))}\n")
            result_file.write(f"Второй файл: {', '.join(map(str, nums2))}\n\n")

            result_file.write("Среднее арифметическое элементов первого и второго файлов:\n")
            result_file.write(f"Первый файл: {avg1:.2f}\n")
            result_file.write(f"Второй файл: {avg2:.2f}\n\n")

            result_file.write("Количество нечетных элементов первого и второго файлов:\n")
            result_file.write(f"Первый файл: {odd_count1}\n")
            result_file.write(f"Второй файл: {odd_count2}\n\n")

            result_file.write("Элементы общие для двух файлов:\n")
            result_file.write(f"{', '.join(map(str, common_elements)) or 'Нет общих элементов'}\n\n")

            result_file.write("Количество элементов, общих для двух файлов:\n")
            result_file.write(f"{common_count}\n")

        print("Обработка файлов завершена. Результаты сохранены в result.txt")

    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except ValueError:
        print("Ошибка: В файле содержатся некорректные данные")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


process_number_files()
