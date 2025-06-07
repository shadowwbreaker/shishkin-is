def process_poem_file():
    try:
        source_filename = 'text18-28.txt'
        poem = [
            "Я помню чудное мгновенье:",
            "Передо мной явилась ты,",
            "Как мимолетное виденье,",
            "Как гений чистой красоты.",
            "",
            "В томленьях грусти безнадежной,",
            "В тревогах шумной суеты,",
            "Звучал мне долго голос нежный",
            "И снились милые черты."
        ]

        with open(source_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(poem))

        with open(source_filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print("Содержимое файла:")
            print(content)
            print(f"\nКоличество символов в тексте: {len(content)}")

        while True:
            try:
                n = int(input("\nВведите номер строки после которой вставить фразу (1-{}): "
                              .format(len(poem))))
                if 1 <= n <= len(poem):
                    break
                print("Номер строки должен быть в диапазоне 1-{}".format(len(poem)))
            except ValueError:
                print("Пожалуйста, введите целое число")

        phrase = input("Введите фразу для вставки: ")

        with open(source_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_filename = 'modified_poem.txt'
        with open(new_filename, 'w', encoding='utf-8') as f:
            for i, line in enumerate(lines, 1):
                f.write(line)
                if i == n:
                    f.write(phrase + '\n')

        print(f"\nФайл '{new_filename}' успешно создан с вставленной фразой после строки {n}")

    except IOError:
        print("Ошибка ввода-вывода при работе с файлом")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

process_poem_file()
