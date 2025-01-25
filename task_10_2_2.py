import json
from json import JSONEncoder
import pickle

from task_10_2_1 import pkl_dump

class Book:
    library = []
    def __init__(self, name, author=None, publishing_house=None, price=None):
        self.name = name
        self.author = author
        self.publishing_house = publishing_house
        self.price = price
        Book.library.append([self.name, self.author, self.publishing_house, self.price])

    @staticmethod
    def get_price(name):
        """
        Возвращает цену книги при ее наличии.
        В противном случае возвращает False.
        """
        for item in Book.library:
            if name in item:
                return f'Цена книги "{name}" = {item[-1]} рублей.'
        return False

    @staticmethod
    def make_order(name, author):
        for item in Book.library:
            if name and author not in item:
                return f'Ваш заказ, книга - "{name}" автора {author} - принят'
        return 'Такая книга есть в нашем магазине. Обратитесь в отдел продаж...'


class Encoder(JSONEncoder):
    def default(self, o):
        try:
            json.dumps(o.__dict__)
            return o.__dict__
        except TypeError:
            return {"Ошибка": "Сериализация не удалась", "Тип объекта": str(type(o))}


book1 = Book(name='Изучаем Python', author='Mark Lutts', publishing_house='O`REILLY', price=1500)
book2 = Book(name='Глубокое обучение', author='Сет Вейдман', publishing_house='O`REILLY', price=1850)
book3 = Book(name='Паттерны разработки на Python', author='Гарри Персиваль', publishing_house='O`REILLY', price=1900)

print(Book.library)         # Получаем цену книги (проверка метода get_price())
print(Book.get_price('Изучаем Python'))
print(Book.get_price('Глубокое обучение'))
print(Book.get_price('Паттерны разработки на Python'))
print(Book.get_price('Фигня всякая'))

books = [book1, book2, book3]
for book in books:
    print('\nJSON. Метод упаковки - ', pack:=json.dumps(book, cls=Encoder), type(pack))     # кодируем json.encoder
    print('JSON. Метод распаковки - ', json.loads(pack), type(json.loads(pack)))            # декодируем json.loads()
    print()
    print('Pickle. Метод упаковки - ', pack_pkl:=pickle.dumps(book), type(pack_pkl))                # кодируем Pickle
    print('Pickle. Метод распаковки - ', pickle.loads(pkl_dump(book)).get_price('Изучаем Python'),
          type(pickle.loads(pkl_dump(book))))                                                       # декодируем Pickle
    print('-'* 100)

