# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

# Объекты в программе должны быть заменяемыми на экземпляры подтипов без влияния на правильность программы.
# Это значит, что объекты производного класса должны иметь возможность заменить объекты базового класса без
# изменения работы программы.

# Создадим пример, в котором не используется данный принцип:
# Создадим класс Bird:

class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print('птица летает')

class Ping(Bird):
    pass

p = Ping("Сара")

p.fly()


# Создадим код с использованием принципа подстановки Барбары Лисков

class Bird():                               # Создадим класс Bird и пропишем, что птица умеет летать

    def fly(self):
        print("эта птица летает")

class Duck(Bird):                           # Создадим класс Duck

    def fly(self):
        print("Эта утка летает быстро")

# Создадим отдельную функцию. Если мы говорим о классе пингвина, в нём вообще не должно быть функции fly.
# Сейчас мы запустим эту функцию fly в целом для чего-то общего. Для этого напишем:
def fly_in_the_sky(animal):
    animal.fly()

# Создадим объекты классов: b = Bird() d = Duck()
b = Bird()
d = Duck()

# Используем функцию "fly in the sky" для каждой птички.
fly_in_the_sky(b)
fly_in_the_sky(d)