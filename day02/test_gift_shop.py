from pathlib import Path

from day02.gift_shop import (
    get_invalid_ids_from_range,
    get_invalid_ids_from_range_2,
    has_repeated_pattern,
    is_id_invalid,
    part1,
    part2,
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


def test_has_repeated_pattern():
    assert has_repeated_pattern("11")
    assert has_repeated_pattern("22")
    assert has_repeated_pattern("99")
    assert has_repeated_pattern("1010")
    assert has_repeated_pattern("1188511885")
    assert has_repeated_pattern("222222")
    assert has_repeated_pattern("446446")
    assert has_repeated_pattern("38593859")
    assert not has_repeated_pattern("1233")
    assert not has_repeated_pattern("1213")
    assert not has_repeated_pattern("1221")
    assert not has_repeated_pattern("222322")
    assert not has_repeated_pattern("232322")
    assert not has_repeated_pattern("222223")
    assert not has_repeated_pattern("57575444")


def test_get_invalid_ids_from_range_2():
    assert get_invalid_ids_from_range_2("11-22") == [11, 22]
    assert get_invalid_ids_from_range_2("95-115") == [99, 111]
    assert get_invalid_ids_from_range_2("998-1012") == [999, 1010]
    assert get_invalid_ids_from_range_2("1188511880-1188511890") == [1188511885]
    assert get_invalid_ids_from_range_2("1698522-1698528") == []
    assert get_invalid_ids_from_range_2("2121212118-2121212124") == [2121212121]
    assert get_invalid_ids_from_range_2("824824821-824824827") == [824824824]


def test_part2():
    sample = sample_file.read_text()
    assert part2(sample) == 4174379265
