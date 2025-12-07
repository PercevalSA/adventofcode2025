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
    """you can find the invalid IDs by looking for any ID which is made only of some
    sequence of digits repeated twice
    """
    result: int = 0
    splitted_data: list[str] = split_data(data)
    all_invalid_ids = []

    for id_range in splitted_data:
        all_invalid_ids.extend(get_invalid_ids_from_range(id_range))

    result = sum(all_invalid_ids)
    return result


def has_repeated_pattern(id_str: str) -> bool:
    # we just need to divide each id by 2 then more until the id length
    id_len = len(id_str)
    pattern_found = False
    for divisor in range(2, id_len + 1):
        window_len = int(id_len / divisor)
        # store first pattern then iterate on the rest
        pattern = id_str[0:window_len]
        logger.debug(f"window length: {window_len}; pattern: {pattern}")

        for i in range(1, divisor):
            logger.debug(f"checking  {id_str[i * window_len : (i + 1) * window_len]}")
            if pattern == id_str[i * window_len : (i + 1) * window_len]:
                pattern_found = True
            else:
                pattern_found = False
                break

        # if we end up here, it means the pattern is repeating until the end
        if pattern_found:
            logger.debug("pattern found!")
            break

    logger.debug(f"returning {pattern_found}")
    return pattern_found


def part2(data: str) -> int:
    """Now, an ID is invalid if it is made only of some sequence of digits repeated
    at least twice
    """

    # on peut pas diviser par 2, il faut trouver le pattern de manière iterative

    return 0
