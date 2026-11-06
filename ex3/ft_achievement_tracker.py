import random

achievements = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer"
]


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice_achievements = gen_player_achievement()
    bob_achievements = gen_player_achievement()
    charlie_achievements = gen_player_achievement()
    dylan_achievements = gen_player_achievement()
    print("Player Alice:", alice_achievements)
    print("Player Bob:", bob_achievements)
    print("Player Charlie:", charlie_achievements)
    print("Player Dylan:", dylan_achievements)
    print()
    print(
        "All distinct achievements:",
        set.union(
            alice_achievements,
            bob_achievements,
            charlie_achievements,
            dylan_achievements,
        ),
    )
    print()
    print(
        "Common achievements:",
        set.intersection(
            alice_achievements,
            bob_achievements,
            charlie_achievements,
            dylan_achievements,
        ),
    )
    print()
    print("Only Alice has:", end=" ")
    print(
        alice_achievements.difference(
            bob_achievements |
            charlie_achievements |
            dylan_achievements
            )
        )
    print("Only Bob has:", end=" ")
    print(
        bob_achievements.difference(
            alice_achievements |
            charlie_achievements |
            dylan_achievements
            )
        )
    print("Only Charlie has:", end=" ")
    print(
        charlie_achievements.difference(
            alice_achievements |
            bob_achievements |
            dylan_achievements
            )
        )
    print("Only Dylan has:", end=" ")
    print(
        dylan_achievements.difference(
            alice_achievements |
            bob_achievements |
            charlie_achievements
            )
        )
    print()

    all_achievements = set(achievements)
    alice_missing = all_achievements.difference(alice_achievements)
    bob_missing = all_achievements.difference(bob_achievements)
    charlie_missing = all_achievements.difference(charlie_achievements)
    dylan_missing = all_achievements.difference(dylan_achievements)
    print("Alice is missing:", alice_missing)
    print("Bob is missing:", bob_missing)
    print("Charlie is missing:", charlie_missing)
    print("Dylan is missing:", dylan_missing)


def gen_player_achievement() -> set[str]:
    quantity = random.randint(5, 9)
    return set(random.sample(achievements, quantity))


if __name__ == "__main__":
    ft_achievement_tracker()
