class Animal:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self):
        return f'Animal(name={self.name}, species={self.species}, age={self.age})'


class Zoo:
    def __init__(self, name: str, max_number_of_animals: int):
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        if len(self.animals) >= self.max_number_of_animals:
            return False
        for с in self.animals:
            if с.name == animal.name and с.species == animal.species:
                return False
        return True

    def add_animal(self, animal: Animal) -> bool:
        if self.can_add_animal(animal):
            self.animals.append(animal)
            return True
        return False

    def can_remove_animal(self, animal: Animal) -> bool:
        return animal in self.animals

    def remove_animal(self, animal: Animal) -> bool:
        if self.can_remove_animal(animal):
            self.animals.remove(animal)
            return True
        return False

    def get_all_animals(self):
        return self.animals

    def get_animals_by_age(self):
        return sorted(self.animals, key=lambda animal: animal.age)

    def get_animals_sorted_alphabetically(self):
        return sorted(self.animals, key=lambda animal: animal.name)



# животные 
tiger = Animal("Aleksandr", "tiger", 7)
flamingo = Animal("Illya", "flamingo", 20)
lion = Animal("Mira", "lion", 5)
zebra = Animal("Gleb", "zebra", 17)

zoo = Zoo("Zoo Tallinn", 3)



# Добавление животных
print(zoo.add_animal(tiger)) 
print(zoo.add_animal(flamingo)) 
print(zoo.add_animal(lion)) 
print(zoo.add_animal(zebra)) # False, превышено макс. количество животных

#алфавит
print(zoo.get_animals_sorted_alphabetically()) 

# Удаление животного
print(zoo.remove_animal(zebra)) # True
print(zoo.remove_animal(zebra)) # False, животное уже удалено

# Получение всех животных
print(zoo.get_all_animals())


print(zoo.get_animals_by_age()) #отсортированные по возрасту меньше большн 

