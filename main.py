from product import Product
from product_manager import ProductManager
from cart import Cart


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
    
     # Create Cart instance
    cart = Cart()

    # Add three products from ProductManager's available products
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

    # Display cart and total value for checkout
    cart.display_cart()
    print(f"\nTotal amount to pay: {cart.calculate_total()}")




if __name__ == "__main__":
    main()