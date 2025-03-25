class Product:    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"Product(Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity})"

class Inventory:
    def __init__(self):
        self.productlist=[]
    def addproduct(self,productobject):
        self.productlist.append(productobject)
        #print(self.productlist)
    def showInventory(self):
        for p in self.productlist:
            print(p)
    def seachProduct(self,pname):
        flag=False
        for p in self.productlist:
            if p.name==pname:
                flag=True
                print('Product found ')
                break
        if flag==False:
            print('Product not found ')       
            
    def updateQuantity(self,pname,newQuantity):
        pass

# Creating an object
product1 = Product("Laptop", 1200, 3)
product2 = Product("Mobile", 50000, 10)
product3 = Product("Bag", 2100, 5)
inventory= Inventory()
inventory.addproduct(product1)
inventory.addproduct(product2)
inventory.addproduct(product3)
inventory.showInventory()
inventory.seachProduct('Bottle')