from pathlib import Path

from day03.lobby import part1, split_data

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_split_data():
    assert split_data(sample_file.read_text()) == [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
        [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
        [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1],
    ]


def test_part1():
    assert part1(sample_file.read_text()) == 0
