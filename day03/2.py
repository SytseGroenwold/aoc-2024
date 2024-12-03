import re
import sys

def process_file(filename):
    # Read the entire file as one string
    with open(filename, 'r') as f:
        content = f.read()
    
    # Toggle starts as True
    calculate_enabled = True
    
    # Regex patterns
    mul_pattern = r'mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Track position as we process the string
    pos = 0
    total = 0
    
    # Find all matches for multiplications and toggles
    mul_matches = list(re.finditer(mul_pattern, content))
    do_matches = list(re.finditer(do_pattern, content))
    dont_matches = list(re.finditer(dont_pattern, content))
    
    # Combine all matches and sort by position
    all_matches = (
        [(m.start(), 'mul', m) for m in mul_matches] +
        [(m.start(), 'do', m) for m in do_matches] +
        [(m.start(), 'dont', m) for m in dont_matches]
    )
    all_matches.sort()  # Sort by position
    
    # Process matches in order
    for pos, match_type, match in all_matches:
        if match_type == 'do':
            calculate_enabled = True
            print("Found do() - enabling calculations")
        elif match_type == 'dont':
            calculate_enabled = False
            print("Found dont() - disabling calculations")
        elif match_type == 'mul' and calculate_enabled:
            # Extract and calculate multiplication
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            product = num1 * num2
            print(f"Found: {match.group(0)} = {product} (enabled)")
            total += product
        elif match_type == 'mul':
            # Just print disabled multiplications
            print(f"Found: {match.group(0)} (disabled)")
    
    return total

def main():
    if len(sys.argv) != 2:
        print("Usage: python 2.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    total = process_file(filename)
    print(f"\nSum of all products: {total}")

if __name__ == "__main__":
    main()
