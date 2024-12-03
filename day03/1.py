# PROMTP:
# I want to create a python program that can solve the following problem. testinput.txt and input.txt are files that contain one big string. Any end of line characters can be considered part of that string. I want you to go through that strin
# g and find all the valid multiplications that are present in the string. A valid multiplication is defined as mul(123,123), where 123 just stands for any integer between 1 and 3 digits. The mul part needs to be exactly mul and the parenthesis
#  are the only accepted symbols around the two integers. Any spaces cannot be ignored and will disqualify any multiplication, so between the parentheses, integers and comma there should be no space. I am thinking about writing a regex that can
#  match all those correct cases. Once a  multiplication is found, I want to print the matched string, then calculate that product, so for mul(17,95) it would be 17*95. The result of that multiplication should be added to a sum of all products
# which I would like returned at the end of the script.

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
