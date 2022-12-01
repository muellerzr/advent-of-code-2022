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