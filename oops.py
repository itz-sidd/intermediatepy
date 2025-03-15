import csv 

class Item:
    pay_rate=0.8#20% discount here
    all=[]
    # pass
    def __init__(self,name:str,price:float,quantity=0):#magic methods
        # print(f"An instance created:{name}")
        assert price >=0,f"Price{price} is not grater than or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not grater than or equal to zero"
        
        #self objects are assigned
        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)
    # def calculate_total_price(self,x,y):#methods
    #     return x*y
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )
        
        @staticmethod
        def is_integer(num):
            if isinstance(num,float):
                return num.is_integer()
            elif isinstance(num,int):
                return True
            else:
                return False

    def __repr__(self):
        return f"Item('{self.name},{self.price},{self.quantity}')"

#item1=Item("Photo",20,5)#instance
# print(item1.apply_discount())
# print(item1.price)
# print(item1.calculate_total_price())
# item1.name="Photo" ... this cant be removed after self.name
# item1.price=20
# item1.quantity=5
#print(item1.calculate_total_price(item1.price,item1.quantity))

# item2=Item("Image",30,10)#instance
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.apply_discount())
#print(item2.price)
# print(item2.calculate_total_price())
# item2.name="Image" ... this cant be removed after self.name
# item2.price=30
# item2.quantity=10
#print(item2.calculate_total_price(item2.price,item2.quantity))

# print(Item.__dict__)#__dict__ works as a dictionary
# print(item1.__dict__)



# item2.has_numpad=False

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)

# random_str="aaa"
# print(random_str.upper())

# print(item1)
# print(type(item1.name))
# print(type(item1.price))



#another list of items
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)
# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7.5))

class Phone(Item):
    all=[]
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):#magic methods
        # print(f"An instance created:{name}")
        assert price >=0,f"Price{price} is not grater than or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not grater than or equal to zero"
        assert broken_phones>=0,f"Broken Phones{broken_phones}"
        #self objects are assigned
        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones=broken_phones

        # Item.all.append(self)
        Phone.all.append(self)


phone1=Phone("samsung",500,5,1)
print(phone1.calculate_total_price())
# phone1.broken_phones=1
phone2=Phone("redmi",700,5,1)
print(phone2.calculate_total_price())
# phone2.broken_phones=1