# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
# Клиенты не должны быть вынуждены зависеть от интерфейсов, которые они не используют.
# Суть в создании специализированных интерфейсов вместо одного, делающего всё подряд.
# Это упрощает внедрение зависимостей и повышает гибкость системы.Объекты в программе должны
# быть заменяемыми на экземпляры подтипов без влияния на правильность программы. Это значит,
# что объекты производного класса должны иметь возможность заменить объекты базового класса без
# изменения работы программы.

# Создадим код без использования данного принципа

class SmartHouse():                    # Создадим класс "Умный дом", внутрь которого мы встроим большое количество функций
    def turn_on_light(self):
        pass

    def heat_food(self):                # Создадим функцию разогрева еды
        pass

    def turn_on_music(self):            # Создадим функцию для включения музыки
        pass
    