# Note: PROMPT just means the next line was a prompt, when using copilot this was not given. It 
# is strictly for clarity.

# PROMPT #
# Given data formatted in groups of 1000 seperated by newlines, find the group with the highest sum

# Read in data
with open("input", "r") as f:
    data = f.read()

# Split data into groups
data = data.split("\n\n")

# Find the group with the highest sum
highest_sum = 0
for group in data:
    group_sum = sum(int(number) for number in group.split())
    if group_sum > highest_sum:
        highest_sum = group_sum

print(highest_sum)

# PROMPT #
# Do it again but in a single line of code

print(max(sum(int(number) for number in group.split()) for group in data.split("\n\n")))