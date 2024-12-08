import sys
from itertools import combinations
import operator
from typing import List, Tuple

def try_operations(numbers: List[int], target: int) -> bool:
    """Try all possible combinations of + and * between numbers in order"""
    if len(numbers) == 1:
        return numbers[0] == target
        
    def evaluate(ops: List[str]) -> int:
        # First pass: handle multiplications
        nums = list(numbers)
        mul_nums = [nums[0]]
        add_ops = []
        
        for i, op in enumerate(ops):
            if op == '*':
                mul_nums[-1] *= nums[i + 1]
            else:  # op == '+'
                mul_nums.append(nums[i + 1])
                add_ops.append(op)
        
        # Second pass: handle additions
        result = mul_nums[0]
        for num in mul_nums[1:]:
            result += num
            
        return result
    
    # Try all possible combinations of + and *
    n = len(numbers) - 1  # number of operators needed
    for i in range(2 ** n):  # each bit represents + (0) or * (1)
        ops = []
        for j in range(n):
            if i & (1 << j):
                ops.append('*')
            else:
                ops.append('+')
        if evaluate(ops) == target:
            return True
            
    return False

def try_combinations(target: int, numbers: List[int]) -> bool:
    """Try all possible operations between numbers"""
    return try_operations(numbers, target)

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
                print(f"Found solution for target {target} with numbers {numbers}")
                total += target

    print(f"Total sum of valid solutions: {total}")

if __name__ == "__main__":
    main()
