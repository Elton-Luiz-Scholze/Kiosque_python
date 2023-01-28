from menu import products


def get_product_by_id(id: int):
    if type(id) is not int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(type_product: str):
    if type(type_product) is not str:
        raise TypeError("product type must be a str")

    products_list = []

    for product in products:
        if product["type"] == type_product:
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
    products_count = len(products)
    prices = 0
    types = []
    count_types = dict({})
    counter = 0
    most_common_type = ""

    for value in products:
        prices += value["price"]
        types.append(value["type"])

    for count_types in types:
        counted_type = types.count(count_types)

        if counted_type > counter:
            counter = counted_type
            most_common_type = count_types

    average_price = round((prices / products_count), 2)

    return f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
