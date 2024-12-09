# PROMPT:
# > Take a look at 01.py. I want to do do something similar in 2.py. First of all it is important to see that the order of the operations does not follow the usual mathematical order. In this script, the order has to be from left to right alway
# s, not * over +. We are also introducing a new operator "||". What it does, is concat two numbers to make one number. An example: 12 || 34 = 1234.

import sys
from itertools import combinations
import operator
from typing import List, Tuple

def try_operations(numbers: List[int], target: int) -> bool:
    """Try all possible combinations of +, * and || between numbers in order"""
    if len(numbers) == 1:
        return numbers[0] == target
        
    def evaluate(ops: List[str]) -> int:
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            else:  # op == '||'
                # Convert both numbers to strings, concatenate, then back to int
                result = int(str(result) + str(numbers[i + 1]))
        return result
    
    # Try all possible combinations of +, * and ||
    n = len(numbers) - 1  # number of operators needed
    for i in range(3 ** n):  # each position can be +, * or ||
        ops = []
        num = i
<<<<<<< HEAD
        for _ in range(n):
            if num % 3 == 0:
                ops.append('+')
            elif num % 3 == 1:
=======
        for j in range(n):
            op_choice = num % 3
            if op_choice == 0:
                ops.append('+')
            elif op_choice == 1:
>>>>>>> 7.2
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
<<<<<<< HEAD
    target, numbers = line.strip().rstrip('`').split(': ')
=======
    target, numbers = line.strip().split(': ')
>>>>>>> 7.2
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
