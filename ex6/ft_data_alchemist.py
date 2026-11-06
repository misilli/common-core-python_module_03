import random

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
    capitalized_names = [player.capitalize() 
                        for player in players
                        ]
    print("New list with all names capitalized:", capitalized_names)

    capitalized_only = [
        player 
        for player in players 
        if player[0].isupper()
    ]
    print("New list of capitalized names only:", capitalized_only)
    score_dict = {
        player : random.randint(1, 100) 
        for player in capitalized_names
    }
    print("Score dict:", score_dict)
    sum_scores = sum(score_dict.values())
    average = sum_scores / len(score_dict)
    print(f"Score average is: {average:.2f}")
    high_scores = {name: score_dict[name] for name in score_dict
                    if score_dict[name] > average}
    print("High scores:", high_scores)



if __name__ == "__main__":
    ft_data_alchemist()