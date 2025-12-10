import logging

logger = logging.getLogger(__name__)


def split_data(data: str) -> list[list[int]]:
    return [list(map(int, list(line))) for line in data.splitlines()]


def search_higher_joltage(batteries_list: list[int]) -> int:
    max_joltage = 0

    # searching for first
    bigger_battery_joltage = 0
    bigger_battery_index = 0
    for index, battery_joltage in enumerate(batteries_list[0:-1]):
        if battery_joltage > bigger_battery_joltage:
            bigger_battery_index = index
            bigger_battery_joltage = battery_joltage

    max_joltage = bigger_battery_joltage

    # searching second
    bigger_battery_joltage = 0

    for battery_joltage in batteries_list[bigger_battery_index + 1 :]:
        if battery_joltage > bigger_battery_joltage:
            bigger_battery_joltage = battery_joltage

    max_joltage = max_joltage * 10 + bigger_battery_joltage

    return max_joltage


def part1(data: str) -> int:
    joltage = 0
    for line in split_data(data):
        joltage += search_higher_joltage(line)
    return joltage


def part2(data: str) -> int:
    return 0
