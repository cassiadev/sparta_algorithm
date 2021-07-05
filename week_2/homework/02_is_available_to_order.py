shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    shop_menus.sort()
    for order in orders:
        if not is_existing_target_number_binary(order, shop_menus):
            return False
    return True


def is_available_to_order_using_set(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2  # 몫 표현

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result1 = is_available_to_order(shop_menus, shop_orders)
result2 = is_available_to_order_using_set(shop_menus, shop_orders)
print(result1, result2)
