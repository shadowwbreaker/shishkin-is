class Animal:
    def __init__(self, species, legs_count, fur_color):
        self.species = species
        self.legs_count = legs_count
        self.fur_color = fur_color

    def __str__(self):
        return f"Вид: {self.species}, Лап: {self.legs_count}, Цвет шерсти: {self.fur_color}"


class Dog(Animal):
    def __init__(self, species, legs_count, fur_color, name, breed):
        super().__init__(species, legs_count, fur_color)
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()}, Кличка: {self.name}, Порода: {self.breed}"


if __name__ == "__main__":
    cat = Animal("Кошка", 4, "серый")
    spider = Animal("Паук", 8, "черный")
    dog1 = Dog("Собака", 4, "белый", "Бобик", "Лабрадор")
    dog2 = Dog("Собака", 4, "коричневый", "Шарик", "Такса")

    print(cat)
    print(spider)
    print(dog1)
    print(dog2)