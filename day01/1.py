#Prompt: I want to iterate over all the lines in this file. The two numbers on each line can be seen as columns. I want to create two lists that contain all the first numbers and all the second numbers. Then I want to sort those two lists, so they both go from smallest to largest number. Then I want to iterate over the length of those lists and compare the difference between the two numbers at every index and take the sum of that difference.

# Open the file "1.input" and iterate over each pair of integers on each row
first_numbers = []
second_numbers = []

with open('1.input', 'r') as file:
    for line in file:
        # Split the line into two integers
        num1, num2 = map(int, line.split())
        # Append the numbers to their respective lists
        first_numbers.append(num1)
        second_numbers.append(num2)

# Sort both lists
first_numbers.sort()
second_numbers.sort()

# Calculate the sum of differences
sum_of_differences = 0
for i in range(len(first_numbers)):
    sum_of_differences += abs(first_numbers[i] - second_numbers[i])

print(f'Sum of differences: {sum_of_differences}')

# Prompt: I want to keep all the old code but add some more code. I next want to calculate a "similarity score". This is a sum of the products of each number from list 1 and the amount of times this number also appears in list two.

# Calculate the similarity score
similarity_score = 0
for num in first_numbers:
    count_in_second = second_numbers.count(num)
    similarity_score += num * count_in_second

print(f'Similarity score: {similarity_score}')
