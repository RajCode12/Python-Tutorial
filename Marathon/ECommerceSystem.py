# Product class with parameters
class Product:
    # constructor 
    def __init__(self,name,price,description):
        self.name = name 
        self.price = price 
        self.description = description
    
    # default print function
    def __str__(self):
        return f"{self.name} {self.price} {self.description}"

# Shopping Cart class
class ShoppingCart:
    def __init__(self):
        self.products = []
        self.inventory = {}
        
    # function to add product to the list
    def add_product(self,product):
        self.products.append(product)
        print('Objects added in cart')
        
        if self.inventory.get(product.name):
            self.inventory[product.name] += 1
        else:
            self.inventory[product.name] = 1

    # function to remove product from the list
    def remove_product(self,product):
        for p in self.products:
            if p.name == product.name:
                self.products.remove(p)
                print('Product removed from cart.')
                break
        
    # function to view cart
    def view_cart(self):
        if len(self.products) < 1:
            print('Cart is empty.')
        else:
            for p in self.products:
                print(p.name,'- $',p.price)
    
    # function to calculate total product price in the cart
    def calculate_total(self):
        total = 0 
        for p in self.products:
            total += p.price 
        print('Total : $', total)
    
    # function to checkout and make cart empty
    def checkout(self):
        self.calculate_total()
        for p in self.products:
            if self.inventory[p.name] is not None:
                self.inventory[p.name] -= 1
        self.products = []
    
    # function to update product inventory
    def update_inventory(self,product,quantity):
        try:
            self.inventory[product.name] = quantity 
        except Exception as e:
            print(e)
    
    # show inventory
    def show_inventory(self):
        for p in self.inventory:
            print(p)

# Test cases 
cart = ShoppingCart()

product1 = Product('Product A',20,'Description A')
product2 = Product('Product B',30,'Description B')
product3 = Product('Product C',100,'Description C')
print('********************************************')

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.view_cart()
print('********************************************')

cart.calculate_total()
print('********************************************')

cart.remove_product(product2)
cart.view_cart()
print('********************************************')

cart.checkout()
cart.view_cart()






