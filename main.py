from management.product_handler import get_product_by_id, get_products_by_type

if __name__ == "__main__":
    print(get_product_by_id(25))
    print(get_product_by_id(0))
    print(get_products_by_type("fruit"))
    print(get_products_by_type("codewars"))
