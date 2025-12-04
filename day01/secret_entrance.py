import logging
from typing import Final

logger = logging.getLogger(__name__)

# The actual password is the number of times the dial is left pointing at 0
# after any rotation in the sequence.

start_position: Final[int] = 50


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
    # direction: R = 1 and L = -1
    direction: int = rot // abs(rot)
    all_clicks: list[int] = [
        (dial_position + i) % 100 for i in range(direction, rot + direction, direction)
    ]

    logger.debug(f"{dial_position};{rotation}: {all_clicks}")
    number_of_zeros: int = all_clicks.count(0)
    logger.debug(f"zeros: {number_of_zeros}")
    return number_of_zeros


def part2(data: str) -> int:
    rotations = data.strip().split("\n")
    dial_position = start_position
    result = 0

    for rotation in rotations:
        result += count_zero_clicks(dial_position, rotation)
        dial_position = move_to_next_position(dial_position, rotation)
        logger.debug(f"dial position: {dial_position}; result: {result}")

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    logger.info(f"Part 1: {part1(data)}")
    logger.info(f"Part 2: {part2(data)}")
