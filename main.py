from management.product_handler import get_product_by_id, get_products_by_type, add_product
from menu import products

new_product = {
    "description": "Espresso coffee, milk, whipped cream and milk or semisweet chocolate",
    "price": 13.50,
    "rating": 5,
    "title": "Coffee mocha",
    "type": "drink",
}

if __name__ == "__main__":
    # print(get_product_by_id(25))
    # print(get_product_by_id(0))
    # print(get_products_by_type("fruit"))
    # print(get_products_by_type("codewars"))
    print(add_product(products, **new_product))
