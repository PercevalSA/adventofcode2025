from pathlib import Path

from day04.printing_department import parse_input

sample_file: Path = Path(__file__).parent / "test_input.txt"


input_list = [
    [False, False, True, False, True, False],
    [True, False, True, False, True, False, True],
    [True, False, True, False, True],
    [True, False, True, False, False, True, False],
    [True, False, True, False, True],
    [False, True, False, True],
    [False, True, False, True, False, True, False, True],
    [True, False, True, False, True],
    [False, True, False],
    [True, False, True, False, True, False, True, False],
]


# parce que j'ai la flemme de générer le dict à la main
def transform_table_to_dict(input_list: list[list]) -> dict:
    my_dict: dict = dict()
    lines = 0
    cols = 0

    for line in input_list:
        for item in line:
            my_dict[(lines, cols)] = item
            cols += 1
        lines += 1

    return my_dict


def test_parse_input():
    data = sample_file.read_text()
    assert transform_table_to_dict(input_list) == parse_input(data)
