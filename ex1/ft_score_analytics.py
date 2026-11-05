import sys


def ft_command_quest() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3",
            " ft_score_analytics.py <score1> <score2> ..."
        )
        return
    print("Scores processed: ", scores)
    print("Total players: ", len(scores))
    print("Total scores: ", sum(scores))
    print("Average score: ", sum(scores) / len(scores))
    print("High score: ", max(scores))
    print("Low score: ", min(scores))
    print("Score range: ", max(scores) - min(scores))


if __name__ == "__main__":
    ft_command_quest()
