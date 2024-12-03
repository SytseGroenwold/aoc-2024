import re
import sys

def process_file(filename):
    # Read the entire file as one string
    with open(filename, 'r') as f:
        content = f.read()
    
    # Regex pattern for valid multiplications
    # Matches 'mul' followed by two 1-3 digit numbers separated by comma in parentheses
    pattern = r'mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)'
    
    # Find all matches
    matches = re.finditer(pattern, content)
    
    total = 0
    for match in matches:
        # Extract the numbers
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        product = num1 * num2
        
        # Print the match and its product
        print(f"Found: {match.group(0)} = {product}")
        total += product
    
    return total

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    total = process_file(filename)
    print(f"\nSum of all products: {total}")

if __name__ == "__main__":
    main()
