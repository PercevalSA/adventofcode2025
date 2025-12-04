from pathlib import Path

from day01.secret_entrance import (
    clicks_from_rotation,
    count_zero_clicks,
    move_to_next_position,
    part1,
    part2,
)

sample_file: Path = Path(__file__).parent / "test_input.txt"


def test_clicks_from_rotation():
    assert clicks_from_rotation("L10") == -10
    assert clicks_from_rotation("R20") == 20
    assert clicks_from_rotation("L70") == -70
    assert clicks_from_rotation("R15") == 15
    assert clicks_from_rotation("L5") == -5


def test_move_to_next_position():
    assert move_to_next_position(50, "L10") == 40
    assert move_to_next_position(40, "R20") == 60
    assert move_to_next_position(60, "L70") == 90
    assert move_to_next_position(90, "R15") == 5
    assert move_to_next_position(5, "L5") == 0


def test_count_zero_clicks():
    assert count_zero_clicks(50, "L60") == 1
    assert count_zero_clicks(10, "L20") == 1
    assert count_zero_clicks(95, "R10") == 1
    assert count_zero_clicks(5, "R10") == 0
    assert count_zero_clicks(30, "R40") == 0
    assert count_zero_clicks(50, "R1000") == 10


def test_part1():
    sample = sample_file.read_text()
    assert part1(sample) == 3


def test_part2():
    sample = sample_file.read_text()
    assert part2(sample) == 6
