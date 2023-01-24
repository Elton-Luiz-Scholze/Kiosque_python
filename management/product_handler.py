from menu import products


def get_product_by_id(id: int):
    for product in products:
        if product["_id"] == id:
            return product
    else:
        return {}


def get_products_by_type(type: str):
    products_list = []

    for product in products:
        if product["type"] == type:
            products_list.append(product)

    return products_list
