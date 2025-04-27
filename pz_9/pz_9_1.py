def create_dictionary():
    ru_en_dict = {
        'яблоко': 'apple',
        'собака': 'dog',
        'кошка': 'cat',
        'дом': 'house',
        'машина': 'car',
        'книга': 'book',
        'вода': 'water',
        'солнце': 'sun',
        'дерево': 'tree',
        'город': 'city'
    }

    print("\nИсходный словарь:")
    for rus, eng in ru_en_dict.items():
        print(f"{rus}: {eng}")

    new_word_rus = 'слон'
    new_word_eng = 'elephant'

    if new_word_rus not in ru_en_dict:
        ru_en_dict[new_word_rus] = new_word_eng
        print(f"\nДобавлено новое слово: '{new_word_rus}': '{new_word_eng}'")
    else:
        print(f"\nСлово '{new_word_rus}' уже есть в словаре")

    print("\nОбновленный словарь:")
    for rus, eng in ru_en_dict.items():
        print(f"{rus}: {eng}")

    return ru_en_dict


dictionary = create_dictionary()