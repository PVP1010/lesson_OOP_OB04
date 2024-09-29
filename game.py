# Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Модификация класса Fighter

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

# Реализация класса Monster

class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"Монстр получает {damage} урона. Осталось {self.health} здоровья.")
        if self.health <= 0:
            print("Монстр побежден!")

    def attack(self):
        return "Монстр атакует!"

# Реализация боя

sword1 = Sword()
bow1 = Bow()

fighter = Fighter(sword1)
monster = Monster(health=50)

print(fighter.attack())
monster.take_damage(20)

fighter.change_weapon(bow1)
print(fighter.attack())
monster.take_damage(30)