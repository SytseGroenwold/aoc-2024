import sys
from itertools import combinations
import operator
from typing import List, Tuple

def try_operations(numbers: List[int], target: int) -> bool:
    """Try all possible combinations of +, * and || between numbers in order"""
    if len(numbers) == 1:
        return numbers[0] == target
        
    def evaluate(ops: List[str]) -> int:
        # First handle || operations to combine numbers
        nums = [str(numbers[0])]
        new_ops = []
        
        for i, op in enumerate(ops):
            if op == '||':
                nums[-1] = nums[-1] + str(numbers[i + 1])
            else:
                nums.append(str(numbers[i + 1]))
                new_ops.append(op)
        
        # Convert strings to integers
        nums = [int(x) for x in nums]
        
        # Then evaluate remaining operations strictly left-to-right
        result = nums[0]
        for i, op in enumerate(new_ops):
            if op == '+':
                result += nums[i + 1]
            else:  # op == '*'
                result *= nums[i + 1]
            
        return result
    
    # Try all possible combinations of +, * and ||
    n = len(numbers) - 1  # number of operators needed
    for i in range(3 ** n):  # each position can be +, * or ||
        ops = []
        num = i
        for _ in range(n):
            if num % 3 == 0:
                ops.append('+')
            elif num % 3 == 1:
                ops.append('*')
            else:
                ops.append('||')
            num //= 3
        if evaluate(ops) == target:
            return True
            
    return False

def try_combinations(target: int, numbers: List[int]) -> bool:
    """Try all possible operations between numbers"""
    return try_operations(numbers, target)

def parse_line(line: str) -> Tuple[int, List[int]]:
    """Parse a line into target number and list of integers"""
    target, numbers = line.strip().rstrip('`').split(': ')
    return int(target), [int(x) for x in numbers.split()]

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
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
