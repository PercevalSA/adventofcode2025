from pathlib import Path

from day02.gift_shop import is_id_invalid, split_range

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_split_range():
    assert split_range("33-54") == [33, 54]


def test_is_id_valid():
    assert is_id_invalid(99)
    assert is_id_invalid(11)
    assert is_id_invalid(22)
    assert is_id_invalid(1010)
    assert not is_id_invalid(115)
    assert not is_id_invalid(998)
    assert not is_id_invalid(1012)


def test_part1():
    pass


def test_part2():
    pass
