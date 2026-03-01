from product import Product
from product_manager import ProductManager


def main():
    # Create ProductManager instance
    manager = ProductManager()

    # Create some products
    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 20)
    product3 = Product("Keyboard", 75, 10)

    # Add products to manager
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Display products
    print("Product List:")
    manager.display_all_products()

    # Display total inventory value
    total_value = manager.calculate_total_value()
    print(f"\nTotal inventory value: {total_value}")


if __name__ == "__main__":
    main()