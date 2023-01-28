from management.product_handler import get_product_by_id


def calculate_tab(kwargs):
    sum = 0

    for value in kwargs:
        product = get_product_by_id(value["_id"])
        sum += product["price"] * value["amount"]

    return {"subtotal": f"${round(sum, 2)}"}
