# PROMPT:
#  > I want to write a script in 1.py that goes through input. lets start with test.input. I want to find all instances of "XMAS" inside this grid of letters. I want to count all instacnes of "XMAS" that are horizontal, vertical or diagonal. Fro
#  horizontal I want to check it both left to right and right to left, for vertical up to down and down to up and also for the diagnocal I want to check both directions. If done right, the test.input should return a total of 18 instances.
#  > it looks like test.input works fine. But 1.input returns 18 XMAS as well and that is way too little. By only searching from left to right horizontal matches manually, I already find 221 matches. What went wrong?

def read_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def check_horizontal(grid):
    count = 0
    for row in grid:
        # Count all occurrences of XMAS from left to right
        for i in range(len(row) - 3):
            if row[i:i+4] == "XMAS":
                count += 1
        # Count all occurrences of SAMX from left to right (right to left reading)
        for i in range(len(row) - 3):
            if row[i:i+4] == "SAMX":
                count += 1
    return count

def check_vertical(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    for col in range(width):
        vertical = ''.join(grid[row][col] for row in range(height))
        # Count top to bottom
        for i in range(len(vertical) - 3):
            if vertical[i:i+4] == "XMAS":
                count += 1
        # Count bottom to top
        for i in range(len(vertical) - 3):
            if vertical[i:i+4] == "SAMX":
                count += 1
    return count

def check_diagonal(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    # Check diagonals going down-right
    for row in range(height - 3):
        for col in range(width - 3):
            # Down-right diagonal
            diagonal = ''.join(grid[row + i][col + i] for i in range(4))
            if diagonal == "XMAS":
                count += 1
            if diagonal == "SAMX":
                count += 1

    # Check diagonals going up-right
    for row in range(3, height):
        for col in range(width - 3):
            # Up-right diagonal
            diagonal = ''.join(grid[row - i][col + i] for i in range(4))
            if diagonal == "XMAS":
                count += 1
            if diagonal == "SAMX":
                count += 1
    return count

def count_xmas_patterns(filename):
    grid = read_grid(filename)
    
    horizontal_count = check_horizontal(grid)
    vertical_count = check_vertical(grid)
    diagonal_count = check_diagonal(grid)
    
    total = horizontal_count + vertical_count + diagonal_count
    print(f"Horizontal matches: {horizontal_count}")
    print(f"Vertical matches: {vertical_count}")
    print(f"Diagonal matches: {diagonal_count}")
    print(f"Total XMAS patterns: {total}")
    return total

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
    count_xmas_patterns(sys.argv[1])
