# Given a set of ID ranges, determine which IDs in another set are within a range.
# E.g.
# 3-5
# 10-14
# 16-20
# 12-18
# 
# 1 (Spoiled)
# 5 (Fresh - 3-5)
# 8 (Spoiled)
# 11 (Fresh - 10-14)
# 17 (Fresh - 12-18, 16-20)
# 32 (Spoiled)
# Range of IDs are inclusive, so 3-5 includes 3,4,5. Ranges can also overlap
# Set 1 is fresh ingredient ranges, and Set 2 is current ingredients
# Determine how many are fresh (Example comes out to 3)

# Outline
# Read the file
# For Set 1:
    # Take each line
    # Add all numbers within range to an array containing all usable IDs
        # Make sure to not add duplicates
# For Set 2:
    # Take each line
    # Check if the line is within the array
    # If in array, add to available ingredients number (or array)
# Count available ingredients number (or count num of items in array)