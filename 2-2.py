def check_sequence(numbers):
    # Convert list of strings to integers
    nums = [int(x) for x in numbers.split()]

    # Create a dictionary of differences between adjacent numbers
    diffs = {i: nums[i+1] - nums[i] for i in range(len(nums)-1)}
    original_diffs = diffs.copy()
    diff_length = len(diffs)
    
    # Remove entries where a number equals its predecessor
    nums = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i-1]]
    # Recalculate differences after removing duplicates
    if len(nums) < diff_length - 1:
        print(f"Zero diffs: {original_diffs.values()}")
        return False #Already return false if there's more than 1 violation
    
    # Remove entries with values smaller than -3 or larger than 3
    nums = [nums[i] for i in range(len(nums)) if i == 0 or abs(nums[i] - nums[i-1]) <= 3]
    if len(nums) < diff_length - 1:
        print(f"Invalid diffs: {original_diffs.values()}")
        return False #Already return false if there's more than 1 violation
    
    # Recalculate differences after removing 0's and differences larger than 3
    diffs = {i: nums[i+1] - nums[i] for i in range(len(nums)-1)}
    # Check if diff holds only positive or negative values
    pos_diffs = all(v > 0 for v in diffs.values())
    neg_diffs = all(v < 0 for v in diffs.values())
    if not (pos_diffs or neg_diffs):
        print(f"Positive and negative diffs: {original_diffs.values()}")
        return False
    
    return True

# Read the file and count valid sequences
valid_count = 0
with open('02.input', 'r') as file:
    for line in file:
        line = line.strip()
        if check_sequence(line):
            print(line)
            valid_count += 1

print(f"Number of valid sequences: {valid_count}")# Read the file and count valid sequences
valid_count = 0
with open('02.input', 'r') as file:
    for line in file:
        line = line.strip()
        if check_sequence(line):
            print(line)
            valid_count += 1

print(f"Number of valid sequences: {valid_count}")
