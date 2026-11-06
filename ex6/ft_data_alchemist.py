
players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    print("Initial list of players: ", players)
    print("New list with all names capitalized:", end=" ")
    for player in players:
        print(f"  {player.capitalize()}" ,end="")

if __name__ == "__main__":
    ft_data_alchemist()