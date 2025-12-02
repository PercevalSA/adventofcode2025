from pathlib import Path

from solution import move_to_next_position, part1

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_move_to_next_position():
    assert move_to_next_position(50, "L10") == 40
    assert move_to_next_position(40, "R20") == 60
    assert move_to_next_position(60, "L70") == 90
    assert move_to_next_position(90, "R15") == 5
    assert move_to_next_position(5, "L5") == 0


def test_part1():
    sample = sample_file.read_text()
    assert part1(sample) == 3


# def test_part2():
#     sample = "example\ndata"
#     assert part2(sample) == expected_value
