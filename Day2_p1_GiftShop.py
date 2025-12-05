# Given a range of numbers, find all numbers within the ranges that are a sequence of numbers repeated twice
# E.g.
# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
# 1/1, 2/2
# 9/9
# 10/10
# 11885/11885
# 222/222
# N/A
# 446/446
# 3859/3859
# The last 3 don't contain any
# Using these numbers, the total output is 1227775554

# Outline
# Read the numbers
# Split into multiple ranges
# Iterate through each range,
    # If the number has an odd number of digits, skip
    # If even, continue
    # Split the number, check if they are equal, add them to a repeated_nums array
# Add the repeated numbers together