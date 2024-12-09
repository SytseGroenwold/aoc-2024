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
            blocks.append((-1, length))  # -1 represents free space
            
    return blocks

def compact_disk(blocks: List[Tuple[int, int]]) -> List[int]:
    """Compact the disk by moving files from right to left."""
    # Convert blocks to flat representation where each number is file ID (-1 for space)
    flat = []
    for file_id, length in blocks:
        flat.extend([file_id] * length)
    
    print(f"Initial disk state: {flat}")
    moves = 0
    
    # Keep moving files until no more moves are possible
    while True:
        moved = False
        # Find rightmost file
        for i in range(len(flat)-1, -1, -1):
            if flat[i] >= 0:  # Found a file block
                # Find leftmost free space
                for j in range(len(flat)):
                    if flat[j] == -1:  # Found free space
                        # Move the file block
                        print(f"Moving file {flat[i]} from position {i} to position {j}")
                        flat[j] = flat[i]
                        flat[i] = -1
                        moved = True
                        moves += 1
                        print(f"Disk state after move {moves}: {flat}")
                        break
                if moved:
                    break
        if not moved:
            print(f"Finished after {moves} moves")
            break
    
    return flat

def calculate_checksum(flat_disk: List[int]) -> int:
    """Calculate checksum by multiplying position by file ID for all file blocks."""
    return sum(pos * file_id 
              for pos, file_id in enumerate(flat_disk) 
              if file_id >= 0)

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
