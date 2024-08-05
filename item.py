import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def __price(self):
        self.price

    def calculate_total_price(self):
        return self.__price * self.quantity


    def __price(self):
        return self.__price
    
    @property
    #Property Decorator = Read-only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increament(self, increament_value):
        self.__price = self.__price + self.__price * increament_value

    @classmethod
    def instantiate_from_csv(cls):
        with open('/home/zoro/Desktop/PROGRAMMING/ALX BACK-END/PYTHON/OOP-PROGRMMING-PYTHON/Item.csv', 'r') as f:
            reader = csv.DictReader(f)    
            items = list(reader)
        
        #Not figured why it won't run yet exact as code on youtube shall keep working on it    
        for item in items:
            '''Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )'''

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @staticmethod
    def is_integer(num):
        #Count out floats that are point zero
        #For i.e 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @classmethod
    def instansiate_from_csv(cls):...
    
    @staticmethod
    def is_integer(num):...


    def __repr__(self):...

    

'''item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''
#print(Item.all)

Item.instantiate_from_csv()
print(Item.all)