#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет 
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства 
#"кличка" и "порода".  
class Animal:
    def __init__(self, type_anim, kol_legs, color):
        self.type_anim = type_anim
        self.kol_legs = kol_legs
        self.color = color
    def __str__(self):
        return f"Вид: {self.type_anim}; Количество лап: {self.kol_legs}; Цвет шерсти: {self.color}."
class Dog(Animal):
    def __init__(self, type_anim, kol_legs, color, name, breed):
        super().__init__(type_anim, kol_legs, color)
        self.name = name
        self.breed = breed
    def __str__(self):
        return (f"Вид: {self.type_anim}; Количество лап: {self.kol_legs}; Цвет шерсти: {self.color}; "
                f"Кличка: {self.name}; Порода: {self.breed}.")
animal = Animal("Хомяк", 4, "Белый")
print(animal)
dog = Dog("Собака", 4, "Белый", "Принц", "Хаски")
print(dog)
