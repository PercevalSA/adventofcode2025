start_position: int = 50

# The actual password is the number of times the dial is left pointing at 0
# after any rotation in the sequence.


def clicks_from_rotation(rotation: str) -> int:
    direction = rotation[:1]
    click_number = int(rotation[1:])
    if direction == "L":
        click_number = -click_number

    return click_number


def move_to_next_position(current_position: int, rotation: str) -> int:
    click_number = clicks_from_rotation(rotation)
    current_position = (current_position + click_number) % 100
    return current_position


def part1(data: str) -> int:
    rotations = data.strip().split("\n")
    dial_position = start_position
    result = 0

    for rotation in rotations:
        dial_position = move_to_next_position(dial_position, rotation)

        if dial_position == 0:
            result += 1

    return result


def count_zero_clicks(dial_position: int, rotation: str) -> int:
    rot: int = clicks_from_rotation(rotation)
    all_clicks: list[int] = list(range(dial_position, dial_position + rot))
    number_of_zeros: int = all_clicks.count(0)
    return number_of_zeros


def part2(data: str) -> int:
    rotations = data.strip().split("\n")
    dial_position = start_position
    result = 0

    for rotation in rotations:
        dial_position = move_to_next_position(dial_position, rotation)
        result += count_zero_clicks(dial_position, rotation)

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
