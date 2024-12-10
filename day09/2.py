# PROMPT:
# > lets make a new file named 2.py and do something similar. The difference now is that entire blocks of numbers  need to be moved at once instead of the individual numbers. Do note that the blocks need to be able to fit inside the empty space
# and that the final state does not end with all the numbers first and empty spaces only at the end. The final checksum is calculated in the same way as well, but whenever there is an empty space, you can just skip it
# > I think I missed sharing some critical info:"This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting wit
# h the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move."

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
    """Compact the disk by moving entire blocks while preserving their sizes."""
    # Convert blocks to flat representation
    flat = []
    for file_id, length in blocks:
        flat.extend([file_id] * length)
    
    # Get list of file blocks with their sizes and positions
    file_blocks = []
    pos = 0
    while pos < len(flat):
        if flat[pos] != '.':
            start = pos
            file_id = flat[pos]
            while pos < len(flat) and flat[pos] == file_id:
                pos += 1
            file_blocks.append((file_id, start, pos - start))
        else:
            pos += 1
    
    # Sort file blocks by ID in descending order
    file_blocks.sort(reverse=True)
    
    # Process each file block
    for file_id, start, size in file_blocks:
        # Find all empty spaces to the left of this file
        spaces = []
        pos = 0
        while pos < start:
            if flat[pos] == '.':
                space_start = pos
                while pos < start and flat[pos] == '.':
                    pos += 1
                spaces.append((space_start, pos - space_start))
            else:
                pos += 1
        
        # Find leftmost space that can fit this file
        for space_start, space_size in spaces:
            if space_size >= size:
                # Move the file to this space
                flat[start:start + size] = ['.'] * size  # Clear original position
                flat[space_start:space_start + size] = [file_id] * size  # Place in new position
                break
    
    return flat

def calculate_checksum(flat_disk: List[int]) -> int:
    """Calculate checksum by multiplying position by file ID for all file blocks."""
    return sum(pos * file_id 
              for pos, file_id in enumerate(flat_disk) 
              if file_id != '.')

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
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
