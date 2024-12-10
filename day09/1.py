# PROMPT:
#  create a script in 1.py, it should take a file name as cli arg as input. Script needs to solve the following problem as explained: He shows you the disk map (your puzzle input) he's already generated. For example:
# 2333133121414131402
# The disk map uses a dense format to represent the layout of files and free space on the disk. The digits alternate between indicating the length of a file and the length of free space.
# So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like 90909 would represent three nine-block files in a row (with no fr
# ee space between them).
# Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged, starting with ID 0. So, the disk map 12345 has three files: a one-block file with ID 0, a three-block file with ID 1, and a fiv
# e-block file with ID 2. Using one character for each block where digits are the file ID and . is free space, the disk map 12345 represents these individual blocks:
# 0..111....22222
# The first example above, 2333133121414131402, represents these individual blocks:
# 00...111...2...333.44.5555.6666.777.888899
# The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:
# 0..111....22222
# 02.111....2222.
# 022111....222..
# 0221112...22...
# 02211122..2....
# 022111222......
# The first example requires a few more steps:
# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............
# The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in posi
# tion 0. If a block contains free space, skip it instead.
# Continuing the first example, the first few blocks' position multiplied by its file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the checksum is the sum of these, 1928.
# Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum?
# > You appear to get stuck in a loop. The script can stop running when all the empty spaces are at the end of the disk state.

import sys
from typing import List, Tuple

def parse_disk_map(disk_map: str) -> List[int]:
    """Convert disk map string into list of integers."""
    return [int(x) for x in disk_map.strip()]

def create_block_representation(lengths: List[int]) -> List[Tuple[int, int]]:
    """Convert alternating file/space lengths into list of (file_id, length) tuples."""
    blocks = []
    file_id = 0
    pos = 0
    
    for i, length in enumerate(lengths):
        if i % 2 == 0:  # File block
            blocks.append((file_id, length))
            file_id += 1
        else:  # Free space
            blocks.append(('.', length))  # '.' represents free space
            
    return blocks

def compact_disk(blocks: List[Tuple[int, int]]) -> List[int]:
    """Compact the disk by moving files from right to left."""
    # Convert blocks to flat representation where each number is file ID ('.' for space)
    flat = []
    for file_id, length in blocks:
        flat.extend([file_id] * length)
    
    # Find first empty space
    space_pos = 0
    while space_pos < len(flat) and flat[space_pos] != '.':
        space_pos += 1
        
    # Keep moving files until all spaces are at the end
    while space_pos < len(flat):
        # Find rightmost file after this space
        file_pos = len(flat) - 1
        while file_pos > space_pos and flat[file_pos] == '.':
            file_pos -= 1
            
        if file_pos <= space_pos:
            break
            
        # Move the file to the empty space
        flat[space_pos] = flat[file_pos]
        flat[file_pos] = '.'
        
        # Find next empty space
        space_pos += 1
        while space_pos < len(flat) and flat[space_pos] != '.':
            space_pos += 1
    
    return flat

def calculate_checksum(flat_disk: List[int]) -> int:
    """Calculate checksum by multiplying position by file ID for all file blocks."""
    return sum(pos * file_id 
              for pos, file_id in enumerate(flat_disk) 
              if file_id != '.')

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
        
    # Read input file
    with open(sys.argv[1], 'r') as f:
        disk_map = f.read().strip()
    
    # Parse input into lengths
    lengths = parse_disk_map(disk_map)
    
    # Convert to blocks with file IDs
    blocks = create_block_representation(lengths)
    
    # Compact the disk
    final_disk = compact_disk(blocks)
    
    # Calculate and print checksum
    checksum = calculate_checksum(final_disk)
    print(checksum)

if __name__ == "__main__":
    main()
