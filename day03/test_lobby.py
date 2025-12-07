from pathlib import Path

from day03.lobby import part1

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_part1():
    assert part1() == 0
