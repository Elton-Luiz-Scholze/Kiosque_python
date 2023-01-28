from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab
from menu import products

new_product = {
    "description": "Espresso coffee, milk, whipped cream and milk or semisweet chocolate",
    "price": 13.50,
    "rating": 5,
    "title": "Coffee mocha",
    "type": "drink",
}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
table_2 = [
    {"_id": 10, "amount": 3},
    {"_id": 20, "amount": 2},
    {"_id": 21, "amount": 5},
]


def main():
    # print(get_product_by_id(25))
    # print(get_product_by_id(0))
    # print(get_products_by_type("fruit"))
    # print(get_products_by_type("codewars"))
    # print(add_product(products, **new_product))
    # print(calculate_tab(table_1))
    # print(calculate_tab(table_2))
    print(menu_report())


if __name__ == "__main__":
    main()
