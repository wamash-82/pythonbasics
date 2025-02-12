class Product:
    def __init__(self,name,price,description,quantity,number):
        self.name=name
        self.price=price
        self.description=description
        self.quantity=quantity
        self.number=number
    def __str__(self):
        return f'{self.name} {self.price} {self.description} {self.quantity} {self.number}'
    def displayinfo(self):
        return f'{self.name} {self.description}'
    def total_price(self):
        return self.price *self.number
    def discount(self,percentage):
        discount=self.price*percentage/100
        final_price=self.price-discount
        return final_price


obj1=Product("Castor oil",1050,"For hair growth","500ml",15)
obj2=Product("Closet",10000,"Cloth storage","6*4",5)
print(obj1)
print(obj2)
print(obj2.displayinfo())
print(obj1.total_price())
print(obj2.total_price())
print(obj2.discount(2))