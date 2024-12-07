import sys
from itertools import combinations
import operator
from typing import List, Tuple

def try_combinations(target: int, numbers: List[int]) -> bool:
    """Try all possible combinations of numbers with + and * operations"""
    ops = [operator.add, operator.mul]
    
    # Try different lengths of combinations
    for length in range(2, len(numbers) + 1):
        # Get all possible combinations of numbers of current length
        for combo in combinations(numbers, length):
            # Try all possible combinations of operations
            stack = [combo[0]]
            for num in combo[1:]:
                for op in ops:
                    new_result = op(stack[-1], num)
                    if new_result == target:
                        return True
                    stack.append(new_result)
    return False

def parse_line(line: str) -> Tuple[int, List[int]]:
    """Parse a line into target number and list of integers"""
    target, numbers = line.strip().split(': ')
    return int(target), [int(x) for x in numbers.split()]

def main():
    if len(sys.argv) != 2:
        print("Usage: python 01.py <input_file>")
        sys.exit(1)

    total = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            target, numbers = parse_line(line)
            if try_combinations(target, numbers):
                total += target

    print(f"Total sum of valid solutions: {total}")

if __name__ == "__main__":
    main()
