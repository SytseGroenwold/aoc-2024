def check_sequence(numbers):
    # Convert list of strings to integers
    nums = [int(x) for x in numbers.split()]
    
    if len(nums) < 2:
        return False
    
    # Check if the sequence is strictly increasing or strictly decreasing
    increasing = all(nums[i] < nums[i+1] for i in range(len(nums)-1))
    decreasing = all(nums[i] > nums[i+1] for i in range(len(nums)-1))
    
    if increasing or decreasing:
        diffs = [abs(nums[i+1] - nums[i]) for i in range(len(nums)-1)]
        return max(diffs) <= 3

# Read the file and count valid sequences
valid_count = 0
with open('02.input', 'r') as file:
    for line in file:
        line = line.strip()
        if check_sequence(line):
            valid_count += 1

print(f"Number of valid sequences: {valid_count}")