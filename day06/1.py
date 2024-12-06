# PROMPT:
# > I want to make a python script that takes a CLI argument as its input file, which will be test.input or 1.input. The python script should read the input file. The input is a map. Dots are open spaces, pound signs are objects and the arrow (
# either ^, >, < or v) is a person walking in that room. The script should make the person walk around following two rules: 1) if there is an empty space in front of them, they move one place forward and 2) if there is an object in front of the
# m (#), right around 90 degrees to the right (this means ^ becomes >, > becomes v  etc). When the person has visited a spot (including its starting spot), the space gets marked with a X to indicate the place has been visited. The person can st
# ill move through this spot after having visited it. Eventually the person will walk off the map, which is the end of the puzzle. I want to see the final map with all its markings and a count of the marked positions (X's) on the map.


import sys
from typing import List, Tuple, Set

def read_map(filename: str) -> List[List[str]]:
    """Read the input file and return as a 2D list."""
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def find_start(grid: List[List[str]]) -> Tuple[int, int, str]:
    """Find starting position and direction of the walker."""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in '^>v<':
                return y, x, grid[y][x]
    raise ValueError("No starting position found")

def get_next_pos(y: int, x: int, direction: str) -> Tuple[int, int]:
    """Get next position based on current direction."""
    if direction == '^':
        return y-1, x
    elif direction == '>':
        return y, x+1
    elif direction == 'v':
        return y+1, x
    else:  # <
        return y, x-1

def turn_right(direction: str) -> str:
    """Turn 90 degrees right."""
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

def is_valid_pos(y: int, x: int, grid: List[List[str]]) -> bool:
    """Check if position is within grid bounds."""
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def walk_map(grid: List[List[str]]) -> Tuple[List[List[str]], int]:
    """Simulate walking through the map and return final state and count of visited positions."""
    y, x, direction = find_start(grid)
    visited = {(y, x)}
    
    while True:
        # Mark current position as visited
        if grid[y][x] not in '#X':
            grid[y][x] = 'X'
        
        # Get next position
        next_y, next_x = get_next_pos(y, x, direction)
        
        # Check if we walked off the map
        if not is_valid_pos(next_y, next_x, grid):
            break
            
        # Check if we need to turn
        if grid[next_y][next_x] == '#':
            direction = turn_right(direction)
            continue
            
        # Move forward
        y, x = next_y, next_x
        visited.add((y, x))
    
    return grid, len(visited)

def print_grid(grid: List[List[str]]):
    """Print the grid."""
    for row in grid:
        print(''.join(row))

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
        
    grid = read_map(sys.argv[1])
    final_grid, visited_count = walk_map(grid)
    
    print("\nFinal map:")
    print_grid(final_grid)
    print(f"\nNumber of positions visited: {visited_count}")

if __name__ == "__main__":
    main()
