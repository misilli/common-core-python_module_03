import sys

def ft_command_quest() -> None:
    print("=== Player Score Analytics ===")
    has_error = False
    for i in range(1, len(sys.argv)):
        try:
            int(sys.argv[i])
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
            has_error = True

    if has_error:
        sys.exit(1)
    
    print("Scores processed: ", sys.argv)
    print("Total players: ", len(sys.argv) - 1)
    print("Total scores: ", sum(sys.argv))
    print("Arguments received: ", len(sys.argv) - 1)
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
    print("Total arguments: ", len(sys.argv))

if __name__ == "__main__":
	ft_command_quest()