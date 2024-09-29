# Создание абстрактного класса для оружия


from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):                    # Sword`: Реализует метод `attack()`, который выводит сообщение о нанесении удара мечом.
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):                       # Bow`: Реализует метод `attack()`, который выводит сообщение о стрельбе из лука.
    def attack(self):
        print("Боец стреляет из лука.")

# Модификация класса Fighter

class Fighter():                          # Класс Fighter: Представляет бойца, который может иметь оружие. У него есть методы:
    def __init__(self, weapon: Weapon):   # Инициализирует бойца с данным оружием.
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):  #  Меняет текущее оружие бойца.
        self.weapon = weapon

    def attack(self):                         #   Вызывает метод `attack()` текущего оружия бойца и выводит соответствующее сообщение.
        print(self.weapon.attack())

# класс монстр
class Monster():                            # **Класс Monster**: Пока является пустым и, вероятно, предназначен для дальнейшего развития программы.
    pass

# Реализация боя
sword1 = Sword()                           # Создаётся объект `Sword
bow1 = Bow()                               # Создаётся объект `Bow
fighter = Fighter(sword1)                  # Создаётся объект fighter` с мечом.
fighter.attack()                           # Боец совершает атаку
fighter.change_weapon(bow1)                # меняет оружие на лук
fighter.attack()                           # Боец совершает атаку