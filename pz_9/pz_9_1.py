inf = {
        "яблоко": "apple",
        "собака": "dog",
        "кошка": "cat",
        "дом": "house",
        "машина": "car",
        "книга": "book",
        "вода": "water",
        "солнце": "sun",
        "дерево": "tree",
        "город": "city"
    }

word = input("Введите слово:")
print(inf.get(word, "Словов не найдено"))
