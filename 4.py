from collections import namedtuple
Cars = namedtuple('CarsA', ('model', 'color','year', 'price'))
c1 = Cars('BMW x7',  'blue',1967,800000)
class Cars:
    def __init__(self, model, price):
        self.name = model
        self.price = price

    def get_price(self):
        return self.price
car1 = Cars("BMW x7", 500000)

print(car1.get_price())  
