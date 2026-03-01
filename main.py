from product import Product
from product_manager import ProductManager


def main():
    # Create ProductManager instance
    manager = ProductManager()

    # Create some products
    product1 = Product("Gaming Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 15)
    product3 = Product("Keyboard", 75, 8)

    # Add products to manager
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)




if __name__ == "__main__":
    main()