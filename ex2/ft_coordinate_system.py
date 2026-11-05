import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        xyz = text.split(",")
        if len(xyz) != 3:
            print("Invalid syntax")
            continue
        try:
            x, y, z = float(xyz[0]), float(xyz[1]), float(xyz[2])
        except ValueError as error:
            bad = str(error).split(": ", 1)[1]
            print(f"Error on parameter {bad}: {error}")
            continue
        return (x, y, z)


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    distance = math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
        )
    return distance


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x, y, z = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {distance((0, 0, 0), pos1):.4f}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance(pos1, pos2):.4f}"
    )


if __name__ == "__main__":
    ft_coordinate_system()
