# Рассмотрим пример кода без использования принципа открытости/закрытости

# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def docPrinter(self):
#         print(f"Отчет сформирован - {self.title} - {self.content}")


# Перепишем созданный класс с учётом принципа открытости/закрытости
# Теперь перепишем созданный класс так, чтобы его можно было самостоятельно дополнять новыми функциями
# — другими словами, используем метод открытости/закрытости.

# Для этого импортируем модуль для работы с абстрактными классами:

from abc import ABC, abstractmethod                  # импортируем модуль

class Formatted(ABC):                                # Создадим абстрактный класс, который будет служить шаблоном для других классов.
    @abstractmethod                                  # (декоратор) дополнения к наим функциям
    def format(self, report):                        # абстрактный метод
        pass

class TextFormatted(Formatted):                      # Создадим обычный класс, который работает с обычным текстом
    def format(self, report):                        # пропишем функцию “формат”
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):                      # Создадим ещё один класс, который будет преобразовывать в формат html
    def format(self, report):
        print(f"<h1>{report.title}</h1>")            #  <h1> — это тэг заголовка, а тэг <p> — это тэг "параграф", то есть тэг обычного текста.
        print(f"<p>{report.content}</p>")

class Report():                                      # Создадим последний, обычный класс В этот класс будет вноситься вся необходимая информация.
    def __init__(self, title, content, formatted):
         self.title = title
         self.content = content
         self.formatted = formatted
#                                     Нам необходимо вызвать функции print, которые находятся внутри функции format. Чтобы их использовать, к классу Report добавим ещё одну функцию:
    def docPrinter(self):
        self.formatted.format(self)

                                                    # Создадим объект класса report, внеся информацию в заголовок и контент
report = Report("заголовок отчёта", "это текст отчёта, его тут много",  TextFormatted())

report.docPrinter()                                 # вызываем функцию def docPrinter

# программа для работы с текстами разных форматов ( Text и HTML)