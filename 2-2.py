def check_sequence(numbers):
    nums = [int(x) for x in numbers.split()]
    
    # First check if sequence is valid as is
    if is_valid_sequence(nums):
        return True
        
    # Try removing one number at a time
    for i in range(len(nums)):
        test_nums = nums[:i] + nums[i+1:]
        if is_valid_sequence(test_nums):
            return True
            
    return False

def is_valid_sequence(nums):
    if len(nums) < 2:
        return True
        
    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    
    # Check if all differences are within -3 to 3
    if any(abs(d) > 3 for d in diffs):
        return False
        
    # Check if sequence is strictly increasing or decreasing
    return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)

# Read the file and count valid sequences
valid_count = 0
with open('02.input', 'r') as file:
    for line in file:
        line = line.strip()
        if check_sequence(line):
            print(line)
            valid_count += 1

print(f"Number of valid sequences: {valid_count}")
