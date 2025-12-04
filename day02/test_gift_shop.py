from pathlib import Path

from day02.gift_shop import (
    get_invalid_ids_from_range,
    is_id_invalid,
    part1,
    split_range,
)

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_split_range():
    assert split_range("33-54") == [33, 54]
    assert split_range("1188511880-1188511890") == [1188511880, 1188511890]


def test_is_id_valid():
    assert is_id_invalid(99)
    assert is_id_invalid(11)
    assert is_id_invalid(22)
    assert is_id_invalid(1010)
    assert not is_id_invalid(115)
    assert not is_id_invalid(998)
    assert not is_id_invalid(1012)


def test_get_invalid_ids_from_range():
    assert get_invalid_ids_from_range("11-22") == [11, 22]
    assert get_invalid_ids_from_range("95-115") == [99]
    assert get_invalid_ids_from_range("998-1012") == [1010]
    assert get_invalid_ids_from_range("1188511880-1188511890") == [1188511885]
    assert get_invalid_ids_from_range("222220-222224") == [222222]
    assert get_invalid_ids_from_range("446443-446449") == [446446]
    assert get_invalid_ids_from_range("1698522-1698528") == []
    assert get_invalid_ids_from_range("38593856-38593862") == [38593859]


def test_part1():
    sample = sample_file.read_text()
    assert part1(sample) == 1227775554


def test_part2():
    pass
