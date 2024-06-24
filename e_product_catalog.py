# Task 1: Create Base Product Class

class Product():

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price 

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")


# Task 2: Implement Subclasses for Specific Products

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

#Task 3: Override Display Method in Subclasses


    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")

# Task 4: Test Product Catalog Functionality

my_book = Book("111", "Think twice", 19.99, "D. Fatade")
my_book.display_info()