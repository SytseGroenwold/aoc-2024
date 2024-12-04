# PROMPT:
# we're continuing with the second part of the puzzle. let's make a new 2.py file and work in there. Instead of finding "XMAS", we now have to find "MAS" in an "X" pattern. One way to achieve this is by thinking of a 3x3 grid, and number each
#  cell from left to right and top to bottom 1-9. cell number 5 will always hold "A". Cell 1 can hold either "M" or "S", but cell 9 will always hold the letter which cell 1 does not hold. This same rule applies to cell 3 and 7. Can you make a r
# epresentation of this pattern in the chat output before you start making the code so I see it as part of my review of your code implementation? You can implement this code in a few file named 2.py.


def read_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def check_x_pattern(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    # For each possible center position of a 3x3 grid
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # Check if center is 'A'
            if grid[row][col] != 'A':
                continue
                
            # Get the corner values
            top_left = grid[row-1][col-1]      # cell 1
            top_right = grid[row-1][col+1]     # cell 3
            bottom_left = grid[row+1][col-1]   # cell 7
            bottom_right = grid[row+1][col+1]  # cell 9
            
            # Check diagonal pairs (1-9 and 3-7)
            # Valid pairs are M-S or S-M
            if ((top_left == 'M' and bottom_right == 'S') or 
                (top_left == 'S' and bottom_right == 'M')):
                if ((top_right == 'M' and bottom_left == 'S') or 
                    (top_right == 'S' and bottom_left == 'M')):
                    count += 1
    
    return count

def count_mas_x_patterns(filename):
    grid = read_grid(filename)
    count = check_x_pattern(grid)
    print(f"Found {count} X patterns")
    return count

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
        sys.exit(1)
    count_mas_x_patterns(sys.argv[1])
