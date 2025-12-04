import logging

logger = logging.getLogger(__name__)


def split_data(data: str) -> list[str]:
    return data.split(",")


def split_range(range: str):
    return [int(id) for id in range.split("-")]


# def iterate_on_ranges(data: list[str]):
#     for range in data:
#         range.split("-")


def is_id_invalid(id: int) -> bool:
    id_str = f"{id}"
    id_len = len(id_str)
    if id_len % 2 != 0:
        logger.debug(f"ID {id} len is odd: {id_len}")
        return False

    half: int = int(id_len / 2)
    logger.debug(f"id: {id}; len: {id_len}; half: {half}")
    return id_str[0:half] == id_str[half:]


def part1(data: str) -> int:
    result: int = 0
    splitted_data: list[str] = split_data(data)

    for id in splitted_data:
        if is_id_invalid(id):
            result += 1

    return result


def part2(data: str) -> int:
    return 0
