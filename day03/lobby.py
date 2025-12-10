import logging

logger = logging.getLogger(__name__)


def split_data(data: str) -> list[list[int]]:
    return [list(map(int, list(line))) for line in data.splitlines()]


def part1(data: str) -> int:
    return 0


def part2(data: str) -> int:
    return 0
