#Книжные магазины предлагают следующие коллекции книг.
#Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
#ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
#БукМаркет – Пушкин, Достоевский, Маяковский.
#Галерея – Чехов, Тютчев, Пушкин.
#Определить в каких магазинах
#нельзя приобрести книги Грибоедова и Маяковского | & -

magistr = {"Лермонтов", "Лермонтов", "Пушкин", "Тютчев"}
DonKnigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BoockMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galery = {"Чехов", "Тютчев", "Пушкин"}

markets = []
if not ({"Грибоедов", "Маяковский"} & magistr):
    markets.append("Магистр")
if not ({"Грибоедов", "Маяковский"} & DonKnigi):
    markets.append("ДомКниги")
if not ({"Грибоедов", "Маяковский"} & BoockMarket):
    markets.append("БукМаркет")
if not ({"Грибоедов", "Маяковский"} & Galery):
    markets.append("Галерея")

print("Магазины, где нельзя приобрести книги Грибоедова и Маяковского:", markets)
