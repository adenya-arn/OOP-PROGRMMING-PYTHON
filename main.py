import csv
#Intr creating and working with classes
# 
# 
# 
"""
class Item:
    def __init__(self, name: str, price: float, quantity = 0):
        #print(f'created {name}')
        
        #Running validations
        assert price >= 0, f"Price{price} is not greater than 0!!"
        assert quantity >= 0, f"Price{quantity} is not greater than 0!!"

        #Assign to self obj
        self.name = name
        self.price = price
        self.quantity = quantity 
          
    def calculate_total_price (self):
            return self.price * self.quantity



item1 = Item("Phone", 100, 5)
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
print(item1.calculate_total_price())
item2 = Item("Laptop", 1000, 3)
print(item2.calculate_total_price())
item2.has_numpad = False






#Creating a class attribute

class Item:
    #DISCOUNT 20%
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity = 0):
        #print(f'created {name}')
        
        #Running validations
        assert price >= 0, f"Price{price} is not greater than 0!!"
        assert quantity >= 0, f"Price{quantity} is not greater than 0!!"

        #Assign to self obj
        self.name = name
        self.price = price
        self.quantity = quantity 
          
    def calculate_total_price (self):
        return self.price * self.quantity
    
    def apply_discount(self):
         self.price = self.price * self.pay_rate
         


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()"""
#print(item2.price)
# print(Item.__dict__)
#print(item1.pay_rate)





# Topic3...........Class and static methods

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('/home/zoro/Desktop/PROGRAMMING/ALX BACK-END/PYTHON/OOP-PROGRMMING-PYTHON/Item.csv', 'r') as f:
            reader = csv.DictReader(f)    
            items = list(reader)
        
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

'''item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''
#print(Item.all)

Item.instantiate_from_csv()
print(Item.all)

