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
    
    # Get list of file blocks with their sizes
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
    
    # Get list of empty spaces with their sizes
    spaces = []
    pos = 0
    while pos < len(flat):
        if flat[pos] == '.':
            start = pos
            while pos < len(flat) and flat[pos] == '.':
                pos += 1
            spaces.append((start, pos - start))
        else:
            pos += 1
    
    def try_arrangement(arrangement, remaining_blocks, remaining_spaces, current_flat):
        if not remaining_blocks:
            checksum = sum(pos * file_id 
                         for pos, file_id in enumerate(current_flat) 
                         if file_id != '.')
            return checksum, current_flat
        
        best_checksum = float('inf')
        best_flat = None
        
        for i, (file_id, _, size) in enumerate(remaining_blocks):
            for j, (space_start, space_size) in enumerate(remaining_spaces):
                if size <= space_size:
                    # Try placing this block in this space
                    new_flat = current_flat.copy()
                    # Clear original position
                    orig_start = arrangement[i][1]
                    new_flat[orig_start:orig_start + size] = ['.'] * size
                    # Place in new position
                    new_flat[space_start:space_start + size] = [file_id] * size
                    
                    # Split remaining space if needed
                    new_spaces = remaining_spaces.copy()
                    new_spaces.pop(j)
                    if space_size > size:
                        new_spaces.append((space_start + size, space_size - size))
                    
                    # Recurse with remaining blocks
                    new_blocks = remaining_blocks.copy()
                    new_blocks.pop(i)
                    checksum, result = try_arrangement(arrangement, new_blocks, new_spaces, new_flat)
                    
                    if checksum < best_checksum:
                        best_checksum = checksum
                        best_flat = result
        
        return best_checksum, best_flat
    
    # Try all possible arrangements
    checksum, result = try_arrangement(file_blocks, file_blocks.copy(), spaces, flat.copy())
    return result if result is not None else flat
    
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
