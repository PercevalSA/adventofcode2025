import logging

logger = logging.getLogger(__name__)


def split_data(data: str) -> list[str]:
    return data.split(",")


def split_range(id_range: str):
    splitted_range = id_range.split("-")
    assert len(splitted_range) == 2
    # TODO: use tuple instead of list
    return [int(id) for id in splitted_range]


def get_invalid_ids_from_range(id_range: str) -> list[int]:
    invalid_ids = []
    [start, end] = split_range(id_range)

    for id in range(start, end + 1):
        if is_id_invalid(id):
            invalid_ids.append(id)

    return invalid_ids


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
    all_invalid_ids = []

    for id_range in splitted_data:
        all_invalid_ids.extend(get_invalid_ids_from_range(id_range))

    result = sum(all_invalid_ids)
    return result


def part2(data: str) -> int:
    return 0
