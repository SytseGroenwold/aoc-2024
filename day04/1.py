def read_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def count_overlapping(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def check_horizontal(grid):
    count = 0
    for row in grid:
        # Left to right
        count += count_overlapping(row, "XMAS")
        # Right to left
        count += count_overlapping(row, "SAMX")
    return count

def check_vertical(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    for col in range(width):
        vertical = ''.join(grid[row][col] for row in range(height))
        # Top to bottom
        count += count_overlapping(vertical, "XMAS")
        # Bottom to top
        count += count_overlapping(vertical, "SAMX")
    return count

def check_diagonal(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    # Check diagonals going down-right and up-left
    for row in range(height):
        for col in range(width):
            if row <= height - 4 and col <= width - 4:
                # Down-right diagonal
                diagonal = ''.join(grid[row + i][col + i] for i in range(4))
                if diagonal == "XMAS":
                    count += 1
                # Check same position for reverse pattern
                if diagonal == "SAMX":
                    count += 1
                    
            if row >= 3 and col <= width - 4:
                # Up-right diagonal
                diagonal = ''.join(grid[row - i][col + i] for i in range(4))
                if diagonal == "XMAS":
                    count += 1
                # Check same position for reverse pattern
                if diagonal == "SAMX":
                    count += 1
    return count

def count_xmas_patterns(filename):
    grid = read_grid(filename)
    
    horizontal_count = check_horizontal(grid)
    vertical_count = check_vertical(grid)
    diagonal_count = check_diagonal(grid)
    
    total = horizontal_count + vertical_count + diagonal_count
    print(f"Found {total} XMAS patterns")
    return total

if __name__ == "__main__":
    count_xmas_patterns("test.input")
