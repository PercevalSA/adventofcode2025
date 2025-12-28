import logging

logger = logging.getLogger(__name__)


def parse_input(data: str) -> dict[tuple[int, int], bool]:
    rolls_map = dict()
    line = 0
    col = 0
    for i in data:
        if i == "\n":
            line += 1
            col = 0

        rolls_map[(line, col)] = True if i == "@" else False

        col += 1

    return rolls_map


def count_rolls_around(rolls_poition: tuple, rolls_map: dict[tuple, bool]) -> int:
    return 0


def part1(data: str) -> int:
    return 0


def part2(data: str) -> int:
    return 0
