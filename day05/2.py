import sys
from itertools import permutations

def parse_input(filename):
    rules = []
    sequences = []
    
    with open(filename, 'r') as file:
        # Read all lines and split into rules and sequences
        content = file.read().strip().split('\n\n')
        
        # Parse rules
        for line in content[0].split('\n'):
            x, y = map(int, line.split('|'))
            rules.append((x, y))
            
        # Parse sequences
        for line in content[1].split('\n'):
            sequence = list(map(int, line.strip().split(',')))
            sequences.append(sequence)
            
    return rules, sequences

def check_sequence(sequence, rules):
    # Check if sequence follows all rules
    for x, y in rules:
        # Find positions of x and y in sequence
        try:
            pos_x = sequence.index(x)
            pos_y = sequence.index(y)
            
            # If y comes before x, rule is violated
            if pos_y < pos_x:
                return False
        except ValueError:
            # If either x or y is not in sequence, skip this rule
            continue
            
    return True

def find_valid_arrangement(sequence, rules):
    # Try all possible permutations of the sequence
    for perm in permutations(sequence):
        if check_sequence(perm, rules):
            return perm
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
        sys.exit(1)
        
    filename = sys.argv[1]
    rules, sequences = parse_input(filename)
    
    # Find invalid sequences and try to fix them
    middle_sum = 0
    for sequence in sequences:
        if not check_sequence(sequence, rules):
            print(f"Invalid sequence: {','.join(map(str, sequence))}")
            valid_arrangement = find_valid_arrangement(sequence, rules)
            if valid_arrangement:
                print(f"Fixed sequence:  {','.join(map(str, valid_arrangement))}")
                
                # Calculate middle number for fixed sequence
                length = len(valid_arrangement)
                if length % 2 == 1:
                    # Odd length - take middle number
                    middle = valid_arrangement[length // 2]
                else:
                    # Even length - take average of two middle numbers
                    mid_right = length // 2
                    mid_left = mid_right - 1
                    middle = (valid_arrangement[mid_left] + valid_arrangement[mid_right]) / 2
                
                middle_sum += middle
            else:
                print("No valid arrangement found!")
            print()
    
    print(f"Sum of middle numbers from fixed sequences: {middle_sum}")

if __name__ == "__main__":
    main()
