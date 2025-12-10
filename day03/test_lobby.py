from pathlib import Path

from day03.lobby import part1, search_higher_joltage, split_data

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_split_data():
    assert split_data(sample_file.read_text()) == [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
        [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
        [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1],
    ]


def test_max_joltage():
    input_data = split_data(sample_file.read_text())

    assert search_higher_joltage(input_data[0]) == 98
    assert search_higher_joltage(input_data[1]) == 89
    assert search_higher_joltage(input_data[2]) == 78
    assert search_higher_joltage(input_data[3]) == 92


def test_max_joltage_12():
    input_data = split_data(sample_file.read_text())

    # assert search_higher_joltage_12(input_data[0]) == 987654321111
    # assert search_higher_joltage_12(input_data[1]) == 811111111119
    # assert search_higher_joltage_12(input_data[2]) == 434234234278
    # assert search_higher_joltage_12(input_data[3]) == 888911112111


def test_part1():
    assert part1(sample_file.read_text()) == 357
