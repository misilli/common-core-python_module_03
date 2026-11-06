import sys


def ft_achievement_tracker() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            split = arg.split(":")
            if len(split) != 2:
                print(f"Error - invalid parameter '{arg}'")
                continue
            name = split[0].strip()
            quantity = int(split[1].strip())
            if name in inventory:
                print(f"Redundant item '{name}' - discarding")
                continue
            inventory[name] = quantity
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))
    total_items = len(inventory)
    total_quantity = sum(inventory.values())
    print(
        f"Total quantity of the {total_items} items: "
        f"{total_quantity}"
    )
    for name in inventory:
        if total_quantity == 0:
            percentage = 0.0
        else:
            percentage = round(inventory[name] / total_quantity * 100, 1)
        print(f"Item {name} represents {percentage}%")
    if inventory:
        temp = next(iter(inventory))
        for name in inventory:
            if inventory[name] > inventory[temp]:
                temp = name
        print(f"Item most abundant: {temp} with quantity {inventory[temp]}")
        temp = next(iter(inventory))
        for name in inventory:
            if inventory[name] < inventory[temp]:
                temp = name
        print(f"Item least abundant: {temp} with quantity {inventory[temp]}")
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    ft_achievement_tracker()
