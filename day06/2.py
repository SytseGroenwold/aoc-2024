import sys
from typing import List, Tuple, Set
from copy import deepcopy

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

def detect_loop(grid: List[List[str]], start_y: int, start_x: int, start_dir: str) -> bool:
    """Simulate walking and detect if we get stuck in a loop."""
    y, x = start_y, start_x
    direction = start_dir
    visited_states = set()
    
    while True:
        # Get next position
        next_y, next_x = get_next_pos(y, x, direction)
        
        # Check if we walked off the map (not a loop)
        if not is_valid_pos(next_y, next_x, grid):
            return False
            
        # Check if we need to turn
        if grid[next_y][next_x] == '#':
            direction = turn_right(direction)
            # Current state is position + direction
            state = (y, x, direction)
            if state in visited_states:
                return True
            visited_states.add(state)
            continue
            
        # Move forward
        y, x = next_y, next_x
        state = (y, x, direction)
        if state in visited_states:
            return True
        visited_states.add(state)

def find_loop_positions(grid: List[List[str]]) -> int:
    """Find sum of positions where adding an object creates a loop."""
    original_grid = deepcopy(grid)
    start_y, start_x, start_dir = find_start(grid)
    loop_sum = 0
    
    # Try each empty position
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if original_grid[y][x] == '.':
                print(f"Testing position ({y}, {x})...", end=" ")
                # Create a new grid with an object at this position
                test_grid = deepcopy(original_grid)
                test_grid[y][x] = '#'
                
                # Check if this creates a loop
                if detect_loop(test_grid, start_y, start_x, start_dir):
                    print("creates loop!")
                    loop_sum += 1
                else:
                    print("no loop")
    
    return loop_sum

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
        sys.exit(1)
        
    grid = read_map(sys.argv[1])
    result = find_loop_positions(grid)
    print(f"Sum of positions causing loops: {result}")

if __name__ == "__main__":
    main()
