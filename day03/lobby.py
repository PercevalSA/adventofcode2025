import logging

logger = logging.getLogger(__name__)


def split_data(data: str) -> list[list[int]]:
    """Convert input text into a list of integer lists."""
    return [[int(ch) for ch in line] for line in data.splitlines()]


def search_higher_joltage(batteries: list[int]) -> int:
    """Return an integer composed of the highest battery (from the prefix)
    followed by the highest battery that appears after it.

    The result is `first * 10 + second`. We search the first battery without the last item
    """
    # consider all candidates for the first value except the last element
    candidates = batteries[:-1]

    # index of the first maximum in candidates
    #
    # __getitem__() is a special method (also known as a dunder or magic method) in Python
    # that allows us to access an element from an object using square brackets,
    # similar to how we access items in a list, tuple, or dictionary.
    # retourne l'index de l'élément max de la liste, car la fonction de comparaison est
    # __getitem__ qui retourne l'item donné à l'index. Les index sont générés grâce à range
    first_index = max(range(len(candidates)), key=candidates.__getitem__)
    first = candidates[first_index]

    # find the maximum after the first_index (may be empty)
    rest = batteries[first_index + 1 :]

    if not rest:
        logger.error(f"empty battery second part: {candidates}")

    second = max(rest)

    logger.debug("first=%s at %s, second=%s", first, first_index, second)
    return first * 10 + second


def search_higher_joltage_12(batteries: list[int]) -> int:
    """cherche le plus grand joltage avec 12 chiffres
    cherche pour chaque fenêtre candidates entre l'index du dernier item trouvé et
    les item restants (12 - le nombre d'item trouvés).
    Puis met à jour la fenêtre jusqu'à qu'il ne reste plus d'items à selectionner
    si le nombre d'item selectionnés + le nombre d'items restant = 12 alors on a finit

    Args:
        batteries (list[int]): liste des batteries

    Returns:
        int: le joltage resultant des 12 batteries sélectionnées
    """
    selected_batteries = 0
    next_bat_index = -1
    next_bat_global_index = 0
    batteries_joltage = 0
    logger.debug(f"searching in {batteries}")

    # we could finish the loop earlier by checking the number of remaining batteries and
    # with that calculation batteries_joltage = batteries_joltage * 10 + int("".join(map(str, candidates)))

    while selected_batteries < 12:
        logger.debug(f"selected batteries: {selected_batteries}")

        # candidates are available batteries: because we need to build a 12 items number
        # we reserve 11 remaining (minus 1 each iteration) so we do not consider the last item
        # after the 4th round

        # we reserve last items so they are not considered as candidates because we need
        # to build a 12 long number
        reserved = 12 - 1 - selected_batteries
        limit_candidates_reserved = len(batteries) - reserved
        reserved_list = batteries[limit_candidates_reserved:]

        logger.debug(
            f"reserved {reserved} ({limit_candidates_reserved}:) {reserved_list}"
        )

        candidates = batteries[next_bat_global_index:limit_candidates_reserved]
        logger.debug(
            f"candidates ( {next_bat_global_index} : {limit_candidates_reserved} ) {candidates}"
        )

        next_bat_index = max(range(0, len(candidates)), key=candidates.__getitem__)
        # compute the selected item's global index within `batteries`
        global_index = next_bat_global_index + next_bat_index
        logger.debug(f"next index: {next_bat_index}; global index: {global_index}")

        batteries_joltage = batteries_joltage * 10 + batteries[global_index]
        logger.debug("battery joltage: {batteries_joltage}")

        selected_batteries += 1
        # next search must start after the selected element
        next_bat_global_index = global_index + 1

    logger.debug(f"found all batteries: {batteries_joltage}")
    return batteries_joltage


def part1(data: str) -> int:
    return sum(search_higher_joltage(line) for line in split_data(data))


def part2(data: str) -> int:
    return sum(search_higher_joltage_12(line) for line in split_data(data))
