import json
import pickle


class Car:
    def __init__(self, vin_number, model, year=None, engine=None, transmission=None,
                 price=None, paid_data=None, check_number=None):
        self.vin_number = vin_number
        self.model = model
        self.year = year
        self.engine = engine
        self.transmission = transmission
        self.price = price
        self.paid_data = paid_data
        self.check_number = check_number
        
    def get_price(self):
        """
        Возвращает цену на автомобиль.
        """
        return self.price

    def get_paid_data(self):
        """
        Возвращает платные данные по машине если была оплата.
        """
        return self.paid_data if self.check_number else False


def make_json_string(obj: object) -> json:
    return json.dumps(obj.__dict__, default=TypeError)

def pkl_dump(obj: object) -> pickle:
    return pickle.dumps(obj)


car1 = Car(vin_number='vin12345', model='audi', year=2025, engine='electro', transmission='robot', price=85000,
           paid_data='very nace car', check_number=12345)

json_string = make_json_string(car1)

print('JSON:')
print(f'Упаковка данных в строку - {type(json_string)}')
print(f'Распаковка данных из строки - {type(json.loads(json_string))}: {json.loads(json_string)}')
print('\nPICKLE:')
dump = pkl_dump(car1)
print(f'Упаковка данных в строку - {dump}')
print(f'Распаковка данных из строки - {pickle.loads(dump).get_price()}')