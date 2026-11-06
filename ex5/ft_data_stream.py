import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while events:
        yield events.pop(random.randint(0, len(events) - 1))


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for event_number in range(1000):
        player, action = next(generator)
        print(f"Event {event_number}: Player {player} did action {action}")

    event_list = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
