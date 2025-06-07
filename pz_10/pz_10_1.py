def find_book_stores():
    try:
        stores = {
            'Магистр': {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'},
            'ДомКниги': {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'},
            'БукМаркет': {'Пушкин', 'Достоевский', 'Маяковский'},
            'Галерея': {'Чехов', 'Тютчев', 'Пушкин'}
        }

        pushkin_stores = {store for store, books in stores.items() if 'Пушкин' in books}
        print("Магазины с книгами Пушкина:", ', '.join(pushkin_stores))

        tytchev_stores = {store for store, books in stores.items() if 'Тютчев' in books}
        print("Магазины с книгами Тютчева:", ', '.join(tytchev_stores))

        both_stores = pushkin_stores & tytchev_stores
        print("\nМагазины, где есть и Пушкин, и Тютчев:", ', '.join(both_stores) if both_stores else "таких магазинов нет")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

find_book_stores()
