import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print("Program name: ", sys.argv[0])
    print("Arguments received: ", len(sys.argv) - 1)
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print("Total arguments: ", len(sys.argv))


if __name__ == "__main__":
    ft_command_quest()
