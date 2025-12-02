def part1(data: str) -> int:
    lines = data.strip().split('\n')
    result = lines
    return result

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    result = lines
    return result

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}") 
