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

def calculate_extended_antinodes(pos1: Tuple[int, int], pos2: Tuple[int, int], grid: List[List[str]]) -> List[Tuple[int, int]]:
    """Calculate all possible antinodes extending in both directions."""
    y1, x1 = pos1
    y2, x2 = pos2
    
    # Calculate the differences (the step size)
    dy = y2 - y1
    dx = x2 - x1
    
    # If both positions are the same, return empty list
    if dy == 0 and dx == 0:
        return []
    
    antinodes = []
    
    # Start from the first position and go backwards
    curr_y, curr_x = y1, x1
    while True:
        curr_y -= dy
        curr_x -= dx
        if not is_valid_position((curr_y, curr_x), grid):
            break
        antinodes.append((curr_y, curr_x))
    
    # Start from the second position and go forwards
    curr_y, curr_x = y2, x2
    while True:
        curr_y += dy
        curr_x += dx
        if not is_valid_position((curr_y, curr_x), grid):
            break
        antinodes.append((curr_y, curr_x))
    
    return antinodes

def is_valid_position(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    """Check if a position is within the grid boundaries."""
    y, x = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def find_unique_antinodes(grid: List[List[str]]) -> int:
    """Find the number of unique valid antinodes in the grid."""
    frequencies = get_frequencies(grid)
    antinodes = set()
    
    # First add all original positions as antinodes
    for positions in frequencies.values():
        for pos in positions:
            antinodes.add(pos)
    
    # Then calculate extended antinodes for each pair
    for positions in frequencies.values():
        # For each pair of positions with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # Calculate all possible antinodes for this pair
                new_antinodes = calculate_extended_antinodes(positions[i], positions[j], grid)
                # Add valid antinodes to the set
                for antinode in new_antinodes:
                    antinodes.add(antinode)
    
    return len(antinodes)

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
        sys.exit(1)
    
    grid = read_grid(sys.argv[1])
    result = find_unique_antinodes(grid)
    print(f"Number of unique valid antinodes: {result}")

if __name__ == "__main__":
    main()
