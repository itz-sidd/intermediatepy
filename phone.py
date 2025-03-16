from item import Item

class Phone(Item):
    # all=[]
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):#magic methods
        # print(f"An instance created:{name}")
        super().__init__(
            name,price,quantity
        )
        assert price >=0,f"Price{price} is not grater than or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not grater than or equal to zero"
        assert broken_phones>=0,f"Broken Phones{broken_phones}"
        #self objects are assigned
        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones=broken_phones