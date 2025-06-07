magistr  = {"Лермонтов", "Лермонтов", "Пушкин", "Тютчев"}
DonKnigi  = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BoockMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galery = {"Чехов", "Тютчев", "Пушкин"}

markets = []
if "Грибоедова" and "Маяковский" not in magistr:
    markets.append("Магистр")
if "Грибоедова" and "Маяковский" not in DonKnigi:
    markets.append("ДомКниги")
if "Грибоедова" and "Маяковский" not in BoockMarket:
    markets.append("БукМаркет")
if "Грибоедова" and "Маяковский" not in Galery:
    markets.append("Галерея")



print("Магазины, где нельзя приобрести книги Грибоедова и Маяковского:", markets)