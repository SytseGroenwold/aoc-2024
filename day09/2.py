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
    
    pos = 0
    while pos < len(flat):
        if flat[pos] == '.':  # Found an empty space
            # Get size of current empty block
            space_size = 0
            space_start = pos
            while pos < len(flat) and flat[pos] == '.':
                space_size += 1
                pos += 1
                
            # Look for the rightmost file block that fits
            scan_pos = len(flat) - 1
            while scan_pos > pos:
                # Find end of current block
                block_end = scan_pos
                while scan_pos > 0 and flat[scan_pos-1] == flat[block_end]:
                    scan_pos -= 1
                block_start = scan_pos
                block_size = block_end - block_start + 1
                
                # If this block fits in the space, move it
                if block_size <= space_size:
                    # Move the block
                    file_id = flat[block_start]
                    flat[space_start:space_start+block_size] = [file_id] * block_size
                    flat[block_start:block_end+1] = ['.'] * block_size
                    break
                
                # Move to next block
                scan_pos = block_start - 1
                while scan_pos > 0 and flat[scan_pos] == '.':
                    scan_pos -= 1
        else:
            pos += 1
    
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
