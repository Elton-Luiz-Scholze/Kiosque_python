from menu import products


def get_product_by_id(id: int):
    if type(id) is not int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type: str):
    products_list = []

    for product in products:
        if product["type"] == type:
            products_list.append(product)

    return products_list


def add_product(products, **kwargs):
    if len(products) == 0:
        kwargs["_id"] = 1

        products.append(kwargs)

        return kwargs

    all_id = []

    for product in products:
        all_id.append(product["_id"])

    id = sorted(all_id)[-1]

    if len(products) > 0:
        kwargs["_id"] = id + 1
        products.append(kwargs)

        return kwargs


def menu_report():
    ...


def add_product_extra():
    ...
