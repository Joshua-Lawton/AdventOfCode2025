# Given a string of numbers, find the largest number possible using 2 digits, from left to right.
# E.g.
# -9--8-7654321111111 - 98
# -8-1111111111111-9- - 89
# 2342342342342-7--8- - 78
# 818181-9-1111-2-111 - 92
# Using these numbers, the total output is 357 (98+89+78+92)

# Outline
# Read the file
# For each line:
    # Take the first highest number (9 preferred) and its index
    # Starting from the place of the first highest, look for the second highest
    # Add to an array
# Add all voltages from the array