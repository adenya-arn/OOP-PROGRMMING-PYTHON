#Topic Inheritance .........


from item import Item

class Phone(Item):
    
    #all = []
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        #Call to super function to have access to all attributes / methods
        
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        assert  broken_phones >= 0, f"Broken {quantity} is not greater or equal to zero!"

        # Assign to self object
        
        self.broken_phones = broken_phones

        # Actions to execute
        #Phone.all.append(self)
    pass





phone1 = Phone("sav10", 500, 5, 1)
print(phone1.calculate_total_price())
#phone1.broken_phones = 1
phone2 = Phone("sav20", 700, 5, 1)
print(phone2.calculate_total_price())
#phone2.broken_phones = 1

#print(Item.all)
#print(Phone.all)