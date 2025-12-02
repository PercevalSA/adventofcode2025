from pathlib import Path

def main():
    print("Hello from adventofcode2025!")
    for day_dir in sorted(Path(".").glob("day*")):
        try:
            solution = __import__(f"{day_dir.name}.solution", fromlist=["part1", "part2"])
            input_file = day_dir / "input.txt"
            if input_file.exists():
                data = input_file.read_text()
                print(f"\n{day_dir.name}:")
                print(f"  Part 1: {solution.part1(data)}")
                print(f"  Part 2: {solution.part2(data)}")
        except Exception as e:
            print(f"{day_dir.name}: Error - {e}")

if __name__ == "__main__":
    main()
