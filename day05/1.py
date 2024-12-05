import sys

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

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
        
    filename = sys.argv[1]
    rules, sequences = parse_input(filename)
    
    # Check each sequence against all rules and collect middle numbers
    middle_sum = 0
    for sequence in sequences:
        if check_sequence(sequence, rules):
            # Print the valid sequence
            print(','.join(map(str, sequence)))
            
            # Calculate middle number
            length = len(sequence)
            if length % 2 == 1:
                # Odd length - take middle number
                middle = sequence[length // 2]
            else:
                # Even length - take average of two middle numbers
                mid_right = length // 2
                mid_left = mid_right - 1
                middle = (sequence[mid_left] + sequence[mid_right]) / 2
            
            middle_sum += middle
    
    print(f"\nSum of middle numbers: {middle_sum}")

if __name__ == "__main__":
    main()
