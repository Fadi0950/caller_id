class Shop:
    shop_name="General Store"
    def __init__(self,id,item_name,item_price,product_name,size):
        self.id=id
        self.name=item_name
        self.price=item_price
        self.product=product_name
        self.size=size

    def getdata(self):
        return self.id,self.name,self.price,self.product,self.size


def call():

 for i in range(1,1000):
  next = input("Do you want to continue Yes/No :")
  if next == 'yes':
   n=int(input("Enter Layer:"))
   x1=int(input("Enter Product id:"))
   x2=input("Enter Name for the Item:")
   x3=int(input("Enter Price of the item:"))
   x4=input("Enter product flavour:")
   x5=input("Enter product size:")
   obj=Shop(x1,x2,x3,x4,x5)
   print(obj.shop_name)
   print(obj.getdata())
  i=+i

call()
