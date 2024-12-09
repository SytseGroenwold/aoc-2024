# PROMPT
# > make a python script in file 01.py. It should take either 1.input or test.input as an argument. The input needs to be considered per line. Every line starts with "int:" which is the solution of a possible equation of the integers after it.
# Of all the integers following the possible solution, check any combination with addition or multiplication to end up at the solution. Print the lines that have a solution and sum the answers of all the possible solutions. Test whether the pro
# gram works with test.input and the final answer being 3749.
# > This took waaay too long. Reconsider what you are doing. I think that for every line you are considering every permutation of numbers, but I forgot to mention that the numbers are already in order and should stay that way. So you just have
# to check all possible placements of either + or * between each numbers and see if that results in the solution at the start of the line


import sys
from itertools import combinations
import operator
from typing import List, Tuple

def try_operations(numbers: List[int], target: int) -> bool:
    """Try all possible combinations of operations between numbers"""
    if len(numbers) == 1:
        return numbers[0] == target
        
    # def evaluate(ops: List[str]) -> int:
    #     # Evaluate strictly left-to-right
    #     result = numbers[0]
    #     for i, op in enumerate(ops):
    #         if op == '+':
    #             result += numbers[i + 1]
    #         else:  # op == '*'
    #             result *= numbers[i + 1]
            
    #     return result
    
    for i in range(1, len(numbers)):
        left = numbers[:i]
        right = numbers[i:]
        
        # Try all possible results from left side
        left_results = get_all_results(left)
        right_results = get_all_results(right)
        
        # Check if any combination of results equals target
        for l in left_results:
            for r in right_results:
                if l + r == target or l * r == target:
                    return True
    
    return False

def get_all_results(numbers: List[int]) -> List[int]:
    """Get all possible results from combining numbers with + and *"""
    if len(numbers) == 1:
        return [numbers[0]]
    
    results = []
    for i in range(1, len(numbers)):
        left = numbers[:i]
        right = numbers[i:]
        
        left_results = get_all_results(left)
        right_results = get_all_results(right)
        
        for l in left_results:
            for r in right_results:
                results.append(l + r)
                results.append(l * r)
    
    return results

def try_combinations(target: int, numbers: List[int]) -> bool:
    """Try all possible combinations of numbers with + and * operations"""
    # Try different lengths of combinations
    for length in range(2, len(numbers) + 1):
        # Get all possible combinations of numbers of current length
        for combo in combinations(numbers, length):
            if try_operations(list(combo), target):
                return True
    return False

def parse_line(line: str) -> Tuple[int, List[int]]:
    """Parse a line into target number and list of integers"""
    target, numbers = line.strip().rstrip('`').split(': ')
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
