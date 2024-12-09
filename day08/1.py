# # PROMPT:
# > We're writing a script in 1.py with either test.input or 1.input as input file, passed along as CLI arguments for the py script. The input can be seen as a map. First I want to create a list of all the different characters in the input. Onl
# y consider digits, lowercase and uppercase characters. We call each of these a frequency. Then I want to gather for each individual frequencies a collection of the coordinates that each occurance of the frequency can be found. Then we need to
#  check for each possible combination of occurances of the same frequencies their antinodes. An antinode can be calculated by doulbing the distance between two occurances. so if the first has coordinates 4,5 and the other 7,6, there would be r
# wo antinodes at 1,4 and the other at 10,7. They are therefore calculated by taking the absolute differnce between the coordinates and then for one antinode adding them, where for the other antinode we substract them. I want these antinodes to
#  be stored all together in one big list. Then finally we can check how many unique entries we have inside this list. Then we count the unique number of antinodes, but we do not consider any antinode that falls outside of our original grid.

import sys
from typing import List, Tuple, Dict, Set
from collections import defaultdict

def read_grid(filename: str) -> List[List[str]]:
    """Read the input file into a 2D grid."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f]

def get_frequencies(grid: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Find coordinates for each frequency (digits, lowercase and uppercase chars)."""
    frequencies = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            char = grid[y][x]
            if char.isalnum():  # Only consider alphanumeric characters
                frequencies[char].append((y, x))
    return frequencies

def calculate_antinodes(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Calculate the two antinodes for a pair of positions."""
    y1, x1 = pos1
    y2, x2 = pos2
    
    # Calculate the differences
    dy = y2 - y1
    dx = x2 - x1
    
    # Calculate the two antinodes
    antinode1 = (y1 - dy, x1 - dx)  # Subtract the differences
    antinode2 = (y2 + dy, x2 + dx)  # Add the differences
    
    return [antinode1, antinode2]

def is_valid_position(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Check if a position is within the grid boundaries."""
    y, x = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def find_unique_antinodes(grid: List[List[str]]) -> int:
    """Find the number of unique valid antinodes in the grid."""
    frequencies = get_frequencies(grid)
    antinodes = set()
    
    # For each frequency
    for positions in frequencies.values():
        # For each pair of positions with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # Calculate antinodes for this pair
                new_antinodes = calculate_antinodes(positions[i], positions[j])
                # Add valid antinodes to the set
                for antinode in new_antinodes:
                    if is_valid_position(antinode, grid):
                        antinodes.add(antinode)
    
    return len(antinodes)

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
    
    grid = read_grid(sys.argv[1])
    result = find_unique_antinodes(grid)
    print(f"Number of unique valid antinodes: {result}")

if __name__ == "__main__":
    main()
