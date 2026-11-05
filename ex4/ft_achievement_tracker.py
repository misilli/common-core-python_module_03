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
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
        inventory[name] = quantity
    
    print()
    print("Got inventory :", inventory)
    print("Item list:", list(inventory.keys()))
    print(f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}")
    for name in inventory.keys():
        print(f"Item {name} represents {round(inventory[name] / sum(inventory.values()) * 100, 1)}%")
    print(f"Item Most abundant item:", max(inventory,  key=inventory.get))

if __name__ == "__main__":
    ft_achievement_tracker()