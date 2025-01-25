import json
import pickle

class Stadium:
    rent_date = []
    sold_seats = []
    def __init__(self, location, max_seating, stadium_type=None):
        self.location = location
        self.max_seating = max_seating
        self.stadium_type = stadium_type

    def adapter_to_dict(self):
        return {
            'location': self.location,
            'max seating': self.max_seating,
            'stadium type': self.stadium_type
        }

    @staticmethod
    def gat_rent(date) -> bool:
        return True if date in Stadium.rent_date else False

    def buy_ticket(self, seating: int):
        if seating not in Stadium.sold_seats and seating < self.max_seating:
            Stadium.sold_seats.append(seating)
            return 'Вы купили билет на стадион'
        return False

stadium1 = Stadium(location='Moscow Luzhniki', max_seating=73189, stadium_type='close type')

print(stadium1.buy_ticket(15))
print(stadium1.buy_ticket(15))

print(pack:=json.dumps(stadium1.adapter_to_dict(), indent=4), type(json.dumps(stadium1.adapter_to_dict())))
print(json.loads(pack), type(json.loads(pack)))
print()
print(pickle.dumps(stadium1))